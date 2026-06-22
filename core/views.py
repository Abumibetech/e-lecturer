import json
import os
import random
import datetime
from io import BytesIO

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q, Avg, Sum, Min
from django.db import IntegrityError
from django.http import JsonResponse, FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings

from .models import (
    Faculty, Department, Programme, Level, Semester,
    Course, CourseModule, Lesson, StudentProfile,
    Enrollment, LessonProgress, CourseQA, PushSubscription,
)


# =========================
# HELPER
# =========================

def unique_courses(queryset=None):
    unique_ids = Course.objects.values('code').annotate(
        first_id=Min('id')
    ).values_list('first_id', flat=True)
    if queryset is not None:
        return queryset.filter(id__in=unique_ids)
    return Course.objects.filter(id__in=unique_ids)


def smart_recommendations(user, limit=6):
    enrollments  = Enrollment.objects.filter(student=user).select_related('course')
    enrolled_ids = enrollments.values_list('course_id', flat=True)

    enrolled_levels    = enrollments.values_list('course__level_id', flat=True).distinct()
    enrolled_semesters = enrollments.values_list('course__semester_id', flat=True).distinct()

    base_qs = unique_courses().exclude(id__in=enrolled_ids)

    priority1 = list(base_qs.filter(
        level_id__in=enrolled_levels,
        semester_id__in=enrolled_semesters
    ))
    priority2 = list(base_qs.filter(
        level_id__in=enrolled_levels
    ).exclude(id__in=[c.id for c in priority1]))
    priority3 = list(base_qs.exclude(
        id__in=[c.id for c in priority1] + [c.id for c in priority2]
    ))

    random.shuffle(priority1)
    random.shuffle(priority2)
    random.shuffle(priority3)

    return (priority1 + priority2 + priority3)[:limit]


# =========================
# HOME
# =========================

def home(request):
    faculties = Faculty.objects.all()
    return render(request, "home.html", {"faculties": faculties})


# =========================
# BROWSING
# =========================

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, "courses/faculty_list.html", {"faculties": faculties})


def department_list(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug)
    departments = Department.objects.filter(faculty=faculty).order_by("name")
    return render(request, "courses/department_list.html", {
        "faculty": faculty, "departments": departments,
    })


def programme_list(request, slug):
    department = get_object_or_404(Department, slug=slug)
    programmes = Programme.objects.filter(department=department).order_by("name")
    return render(request, "courses/programme_list.html", {
        "department": department, "programmes": programmes,
    })


def level_courses(request, programme_id, level):
    programme = get_object_or_404(Programme, id=programme_id)
    level_obj = get_object_or_404(Level, name=level)
    courses   = unique_courses(Course.objects.filter(
        programmecourse__programme=programme, level=level_obj
    ))
    return render(request, "courses/level_courses.html", {
        "programme": programme, "level": level_obj, "courses": courses,
    })


# =========================
# COURSE DETAILS
# =========================

@login_required
def course_detail(request, pk):
    course     = get_object_or_404(Course, pk=pk)
    modules    = CourseModule.objects.filter(course=course).order_by("order")
    qa_count   = CourseQA.objects.filter(course=course, is_published=True).count()
    enrollment = Enrollment.objects.filter(student=request.user, course=course).first()
    return render(request, "courses/course_detail.html", {
        "course": course, "modules": modules,
        "qa_count": qa_count, "enrollment": enrollment,
    })


# =========================
# ENROLLMENT
# =========================
@login_required
def enroll_course(request, course_id):
    StudentProfile.objects.get_or_create(user=request.user)
    course = get_object_or_404(Course, id=course_id)
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user, course=course,
    )
    if created:
        enrollment.progress = 0
        enrollment.completed = False
        enrollment.save()
        messages.success(request, f"Successfully enrolled in {course.code}!")
    else:
        messages.info(request, "You are already enrolled in this course.")
    return redirect("my_courses")


# =========================
# COURSE PLAYER
# =========================

@login_required
def course_player(request, pk, lesson_id=None):
    course     = get_object_or_404(Course, id=pk)
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    enrollment = Enrollment.objects.filter(student=request.user, course=course).first()

    if not enrollment:
        messages.warning(request, "Please enroll first.")
        return redirect("explore")

    modules = CourseModule.objects.filter(course=course).order_by("order")
    lessons = Lesson.objects.filter(module__course=course).order_by("order")

    current_lesson = None
    if lesson_id:
        current_lesson = lessons.filter(id=lesson_id).first()
    if not current_lesson:
        current_lesson = lessons.first()

    lesson_list = list(lessons)
    next_lesson = prev_lesson = None

    if current_lesson and current_lesson in lesson_list:
        idx         = lesson_list.index(current_lesson)
        next_lesson = lesson_list[idx + 1] if idx + 1 < len(lesson_list) else None
        prev_lesson = lesson_list[idx - 1] if idx > 0 else None

    current_progress = None
    if current_lesson:
        current_progress, _ = LessonProgress.objects.get_or_create(
            student=profile, lesson=current_lesson
        )
        total     = lessons.count()
        completed = LessonProgress.objects.filter(
            student=profile, lesson__module__course=course, is_completed=True
        ).count()
        progress = int((completed / total) * 100) if total > 0 else 0
        enrollment.progress  = progress
        enrollment.completed = (progress == 100)
        enrollment.save()

    completed_lesson_ids = set(
        LessonProgress.objects.filter(
            student=profile, lesson__module__course=course, is_completed=True
        ).values_list('lesson_id', flat=True)
    )

    return render(request, "courses/course_player.html", {
        "course": course, "modules": modules, "lessons": lessons,
        "current_lesson": current_lesson, "next_lesson": next_lesson,
        "prev_lesson": prev_lesson, "enrollment": enrollment,
        "current_progress": current_progress,
        "completed_lesson_ids": completed_lesson_ids,
    })


# =========================
# SAVE VIDEO RESUME POSITION
# =========================

@login_required
@csrf_exempt
def save_video_position(request, lesson_id):
    """Called via JS every few seconds while video plays — saves resume point."""
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data       = json.loads(request.body)
        position   = float(data.get("position", 0))
        profile, _ = StudentProfile.objects.get_or_create(user=request.user)
        lesson     = get_object_or_404(Lesson, id=lesson_id)
        progress_obj, _ = LessonProgress.objects.get_or_create(student=profile, lesson=lesson)
        progress_obj.last_position = position
        progress_obj.save(update_fields=["last_position"])
        return JsonResponse({"status": "saved"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# =========================
# MARK LESSON COMPLETE
# =========================

@login_required
def mark_lesson_complete(request, course_id, lesson_id):
    """Mark Complete button — sets is_completed True and recalculates course progress."""
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    lesson     = get_object_or_404(Lesson, id=lesson_id)
    course     = get_object_or_404(Course, id=course_id)

    progress_obj, _ = LessonProgress.objects.get_or_create(student=profile, lesson=lesson)
    progress_obj.is_completed = True
    progress_obj.save()

    enrollment = Enrollment.objects.filter(student=request.user, course=course).first()
    if enrollment:
        lessons   = Lesson.objects.filter(module__course=course)
        total     = lessons.count()
        completed = LessonProgress.objects.filter(
            student=profile, lesson__module__course=course, is_completed=True
        ).count()
        enrollment.progress  = int((completed / total) * 100) if total > 0 else 0
        enrollment.completed = (enrollment.progress == 100)
        enrollment.save()
        messages.success(request, f"✅ Marked '{lesson.title}' as complete!")

    return redirect("course_player_lesson", pk=course_id, lesson_id=lesson_id)


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):
    profile, _  = StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(student=request.user).select_related("course")

    avg          = enrollments.aggregate(Avg("progress"))["progress__avg"] or 0
    total_hours  = enrollments.aggregate(Sum("hours_learned"))["hours_learned__sum"] or 0
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()

    recommended_courses = smart_recommendations(request.user, limit=6)

    return render(request, "dashboard/index.html", {
        "enrollments":         enrollments,
        "avg_progress":        round(avg),
        "total_hours":         round(total_hours, 1),
        "completed_courses":   enrollments.filter(completed=True).count(),
        "total_enrolled":      enrollments.count(),
        "profile":             profile,
        "recommended_courses": recommended_courses,
        "push_enabled":        push_enabled,
    })


# =========================
# MY COURSES
# =========================

@login_required
def my_courses(request):
    StudentProfile.objects.get_or_create(user=request.user)
    enrollments = Enrollment.objects.filter(
        student=request.user
    ).select_related("course").order_by("-id")
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()
    return render(request, "dashboard/my_courses.html", {
        "enrollments": enrollments,
        "push_enabled": push_enabled,
    })


# =========================
# EXPLORE
# =========================

@login_required
def explore(request):
    StudentProfile.objects.get_or_create(user=request.user)
    enrolled_ids = Enrollment.objects.filter(
        student=request.user
    ).values_list("course_id", flat=True)

    courses = unique_courses().exclude(id__in=enrolled_ids)
    query   = request.GET.get("q")
    if query:
        courses = courses.filter(
            Q(title__icontains=query) | Q(code__icontains=query) | Q(description__icontains=query)
        )
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()
    return render(request, "dashboard/explore.html", {
        "courses": courses, "push_enabled": push_enabled,
    })


# =========================
# PROGRESS
# =========================

@login_required
def progress(request):
    profile, _   = StudentProfile.objects.get_or_create(user=request.user)
    enrollments  = Enrollment.objects.filter(student=request.user).select_related("course")
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()
    return render(request, "dashboard/progress.html", {
        "enrollments": enrollments,
        "total_lessons_completed": LessonProgress.objects.filter(
            student=profile, is_completed=True
        ).count(),
        "total_lessons": LessonProgress.objects.filter(student=profile).count(),
        "push_enabled": push_enabled,
    })


# =========================
# COURSE Q&A
# =========================

@login_required
def course_qa(request, course_id):
    course  = get_object_or_404(Course, id=course_id)
    qa_list = CourseQA.objects.filter(
        course=course, is_published=True
    ).order_by("order", "-created_at")
    enrollment   = Enrollment.objects.filter(student=request.user, course=course).first()
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()
    return render(request, "courses/course_qa.html", {
        "course": course, "qa_list": qa_list,
        "enrollment": enrollment, "push_enabled": push_enabled,
    })


# =========================
# COURSE Q&A — PDF DOWNLOAD
# =========================

@login_required
def course_qa_pdf(request, course_id):
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable
    )

    course  = get_object_or_404(Course, id=course_id)
    qa_list = CourseQA.objects.filter(
        course=course, is_published=True
    ).order_by("order", "-created_at")

    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4,
        topMargin=20 * mm, bottomMargin=20 * mm,
        leftMargin=18 * mm, rightMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "QATitle", parent=styles["Heading1"],
        fontSize=18, leading=22, textColor=colors.HexColor("#0a0f1e"),
        spaceAfter=4,
    )
    sub_style = ParagraphStyle(
        "QASub", parent=styles["Normal"],
        fontSize=10, textColor=colors.HexColor("#666666"),
        spaceAfter=2,
    )
    section_title_style = ParagraphStyle(
        "SectionTitle", parent=styles["Heading2"],
        fontSize=13, leading=16, textColor=colors.HexColor("#0a0f1e"),
        spaceBefore=14, spaceAfter=6,
    )
    badge_style = ParagraphStyle(
        "Badge", parent=styles["Normal"],
        fontSize=8, textColor=colors.HexColor("#00a896"),
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "Body", parent=styles["Normal"],
        fontSize=10.5, leading=16, textColor=colors.HexColor("#222222"),
        spaceAfter=10,
    )

    elements = []

    logo_path = os.path.join(settings.BASE_DIR, "static", "images", "e-lecturer.png")

    if os.path.exists(logo_path):
        header_table_data = [[
            Image(logo_path, width=42, height=42),
            Paragraph(
                "<font size=16><b>E-Lecturer</b></font><br/>"
                "<font size=9 color='#666666'>Smart Learning Platform</font>",
                styles["Normal"]
            ),
        ]]
        header_table = Table(header_table_data, colWidths=[50, 400])
        header_table.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (0, 0), 0),
            ("LEFTPADDING", (1, 0), (1, 0), 10),
        ]))
        elements.append(header_table)
    else:
        elements.append(Paragraph("<b>E-Lecturer</b>", title_style))

    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", color=colors.HexColor("#00c2ff"), thickness=1.4))
    elements.append(Spacer(1, 14))

    elements.append(Paragraph(f"{course.code} — {course.title}", title_style))
    elements.append(Paragraph("Questions &amp; Answers / Course Summary", sub_style))
    elements.append(Paragraph(
        f"Generated for: {request.user.first_name or request.user.username} &nbsp;|&nbsp; "
        f"Date: {datetime.datetime.now().strftime('%d %B %Y')}",
        sub_style
    ))
    elements.append(Spacer(1, 18))

    if not qa_list:
        elements.append(Paragraph(
            "No Q&amp;A or summary content has been published for this course yet.",
            body_style
        ))
    else:
        for idx, qa in enumerate(qa_list, start=1):
            label = "SUMMARY / NOTES" if qa.content_type == "summary" else "QUESTIONS & ANSWERS"
            elements.append(Paragraph(f"{idx}. {qa.title}", section_title_style))
            elements.append(Paragraph(label, badge_style))

            content_html = qa.content.replace("\n", "<br/>")
            elements.append(Paragraph(content_html, body_style))
            elements.append(HRFlowable(
                width="100%", color=colors.HexColor("#e5e7eb"), thickness=0.6
            ))
            elements.append(Spacer(1, 10))

    elements.append(Spacer(1, 20))
    elements.append(HRFlowable(width="100%", color=colors.HexColor("#cccccc"), thickness=0.5))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "<font size=8 color='#999999'>Downloaded from E-Lecturer — your smart study companion.</font>",
        styles["Normal"]
    ))

    doc.build(elements)
    buffer.seek(0)

    filename = f"{course.code}_QA_{course.title[:30].replace(' ', '_')}.pdf"
    return FileResponse(buffer, as_attachment=True, filename=filename)


# =========================
# COURSE Q&A — TXT DOWNLOAD
# =========================

@login_required
def download_course_qa(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    qa_list = CourseQA.objects.filter(course=course, is_published=True).order_by("order", "-created_at")

    text = []
    text.append(
f"""
========================
E-LECTURER
{course.code}
{course.title}
========================

"""
    )

    for i, q in enumerate(qa_list, 1):
        text.append(
f"""

{i}. {q.title}

{q.content}

------------------------

"""
        )

    response = HttpResponse("\n".join(text), content_type="text/plain")
    response["Content-Disposition"] = f'attachment; filename="{course.code}_QA.txt"'
    return response


# =========================
# AI LECTURER
# =========================

@login_required
def ai_lecturer(request):
    StudentProfile.objects.get_or_create(user=request.user)
    enrollments  = Enrollment.objects.filter(student=request.user).select_related("course")
    push_enabled = PushSubscription.objects.filter(user=request.user).exists()

    courses_data = []
    for e in enrollments:
        modules      = CourseModule.objects.filter(course=e.course).prefetch_related("lessons")
        modules_data = []
        for m in modules:
            lessons_list = [{"title": l.title, "description": l.description or ""} for l in m.lessons.all()]
            modules_data.append({"module": m.title, "lessons": lessons_list})
        courses_data.append({
            "code": e.course.code, "title": e.course.title,
            "description": e.course.description or "",
            "progress": round(e.progress), "completed": e.completed,
            "modules": modules_data,
        })

    return render(request, "dashboard/ai_lecturer.html", {
        "enrollments":  enrollments,
        "courses_json": json.dumps(courses_data),
        "student_name": request.user.first_name or request.user.username,
        "push_enabled": push_enabled,
    })


# =========================
# AI CHAT API
# =========================

@login_required
@csrf_exempt
def ai_chat(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        body          = json.loads(request.body)
        chat_messages = body.get("messages", [])
        system        = body.get("system", "")

        if not chat_messages:
            return JsonResponse({"error": "No messages provided"}, status=400)

        provider = getattr(settings, "AI_PROVIDER", "groq")

        if provider == "groq":
            api_key    = getattr(settings, "GROQ_API_KEY", None)
            model_name = getattr(settings, "GROQ_MODEL", "llama-3.3-70b-versatile")
            if not api_key:
                return JsonResponse({"error": "GROQ_API_KEY not set."}, status=500)
            try:
                from groq import Groq
            except ImportError:
                return JsonResponse({"error": "Run: pip install groq"}, status=500)

            client        = Groq(api_key=api_key)
            groq_messages = [{"role": "system", "content": system}]
            for msg in chat_messages:
                role    = msg.get("role", "user")
                content = msg.get("content", "")
                if isinstance(content, list):
                    text_parts = [p["text"] for p in content if isinstance(p, dict) and p.get("type") == "text"]
                    groq_messages.append({"role": role, "content": " ".join(text_parts)})
                else:
                    groq_messages.append({"role": role, "content": content})

            completion = client.chat.completions.create(
                model=model_name, messages=groq_messages, max_tokens=2000, temperature=0.7,
            )
            return JsonResponse({"reply": completion.choices[0].message.content})

        elif provider == "gemini":
            api_key    = getattr(settings, "GEMINI_API_KEY", None)
            model_name = getattr(settings, "GEMINI_MODEL", "gemini-2.0-flash")
            if not api_key:
                return JsonResponse({"error": "GEMINI_API_KEY not set"}, status=500)
            try:
                import google.generativeai as genai
            except ImportError:
                return JsonResponse({"error": "Run: pip install google-generativeai"}, status=500)

            genai.configure(api_key=api_key)
            full_prompt = system + "\n\n"
            for msg in chat_messages:
                role    = msg.get("role", "user")
                content = msg.get("content", "")
                prefix  = "Student: " if role == "user" else "E-Lecturer AI: "
                if isinstance(content, list):
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            full_prompt += f"{prefix}{part['text']}\n\n"
                else:
                    full_prompt += f"{prefix}{content}\n\n"
            full_prompt += "E-Lecturer AI: "
            model    = genai.GenerativeModel(model_name)
            response = model.generate_content(full_prompt)
            return JsonResponse({"reply": response.text})

        else:
            return JsonResponse({"error": f"Unknown AI_PROVIDER: '{provider}'"}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        import traceback
        print("AI CHAT ERROR:", traceback.format_exc())
        return JsonResponse({"error": str(e)}, status=500)


# =========================
# AUTH
# =========================

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email     = request.POST.get("email", "").strip().lower()
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if not full_name or not email or not password1:
            messages.error(request, "All fields are required.")
            return redirect("register")
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect("register")

        try:
            names      = full_name.split()
            first_name = names[0]
            last_name  = " ".join(names[1:]) if len(names) > 1 else ""
            user = User.objects.create_user(
                username=email, email=email, password=password1,
                first_name=first_name, last_name=last_name,
            )
            StudentProfile.objects.get_or_create(user=user)
            login(request, user)
            return redirect("dashboard")
        except IntegrityError:
            messages.error(request, "Registration failed. Please try again.")
            return redirect("register")

    return render(request, "auth/register.html")


def login_view(request):
    if request.method == "POST":
        email    = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        user     = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            StudentProfile.objects.get_or_create(user=user)
            return redirect("dashboard")
        messages.error(request, "Invalid email or password.")
    return render(request, "auth/login.html")


# =========================
# LESSON & LOGOUT & DROP
# =========================

@login_required
def toggle_lesson_complete(request, lesson_id):
    profile, _ = StudentProfile.objects.get_or_create(user=request.user)
    lesson      = get_object_or_404(Lesson, id=lesson_id)
    progress_obj, _ = LessonProgress.objects.get_or_create(student=profile, lesson=lesson)
    progress_obj.is_completed = not progress_obj.is_completed
    progress_obj.save()
    return redirect(request.META.get("HTTP_REFERER", "dashboard"))


@login_required
def logout_confirm(request):
    return render(request, "dashboard/logout.html")


def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def drop_course(request, enrollment_id):
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user)
    if request.method == "POST":
        enrollment.delete()
    return redirect('my_courses')


# =========================
# PUSH NOTIFICATIONS
# =========================

@login_required
def push_vapid_key(request):
    return JsonResponse({"publicKey": getattr(settings, "VAPID_PUBLIC_KEY", "")})


@login_required
@csrf_exempt
@require_POST
def push_subscribe(request):
    try:
        data     = json.loads(request.body)
        endpoint = data.get("endpoint")
        p256dh   = data.get("keys", {}).get("p256dh")
        auth     = data.get("keys", {}).get("auth")

        if not all([endpoint, p256dh, auth]):
            return JsonResponse({"error": "Missing subscription fields"}, status=400)

        sub, created = PushSubscription.objects.update_or_create(
            endpoint=endpoint,
            defaults={"user": request.user, "p256dh": p256dh, "auth": auth},
        )
        try:
            from .tasks import _send_push
            _send_push(sub, title="🔔 Notifications Enabled!",
                       body="You'll receive daily study reminders and milestone alerts. Let's go! 📚",
                       url="/dashboard/")
        except Exception:
            pass
        return JsonResponse({"status": "subscribed", "created": created})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@login_required
@csrf_exempt
@require_POST
def push_unsubscribe(request):
    try:
        data     = json.loads(request.body)
        endpoint = data.get("endpoint")
        if endpoint:
            PushSubscription.objects.filter(user=request.user, endpoint=endpoint).delete()
        return JsonResponse({"status": "unsubscribed"})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@login_required
def gpa_calculator(request):
    return render(request, "dashboard/gpa_calculator.html")