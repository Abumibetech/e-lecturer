import io
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html
from django.db.models import Avg
from django.urls import path
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User

from .models import (
    Faculty,
    Department,
    Programme,
    Level,
    Semester,
    Course,
    ProgrammeCourse,
    CourseModule,
    Lesson,
    StudentProfile,
    Enrollment,
    LessonProgress,
    CourseQA,
)


# =========================
# CUSTOM ADMIN SITE
# =========================

class ELecturerAdminSite(AdminSite):
    site_header = "E-Lecturer Admin"
    site_title = "E-Lecturer"
    index_title = "Welcome to E-Lecturer Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path('activity/', self.admin_view(self.activity_view), name='student_activity'),
        ]
        return custom + urls

    def activity_view(self, request):
        total_students = StudentProfile.objects.count()
        total_enrollments = Enrollment.objects.count()
        total_completions = Enrollment.objects.filter(completed=True).count()
        total_lessons_done = LessonProgress.objects.filter(is_completed=True).count()
        overall_avg = round(
            Enrollment.objects.aggregate(avg=Avg("progress"))["avg"] or 0
        )

        top_students = []
        for profile in StudentProfile.objects.select_related("user").all():
            enrollments = Enrollment.objects.filter(student=profile.user)
            lessons_done = LessonProgress.objects.filter(
                student=profile, is_completed=True
            ).count()
            avg = enrollments.aggregate(avg=Avg("progress"))["avg"] or 0
            top_students.append({
                "name": profile.user.first_name or profile.user.username,
                "email": profile.user.email,
                "courses": enrollments.count(),
                "completed": enrollments.filter(completed=True).count(),
                "lessons": lessons_done,
                "avg_progress": round(avg),
            })
        top_students = sorted(
            top_students, key=lambda x: x["lessons"], reverse=True
        )[:15]

        top_courses = []
        for course in Course.objects.all():
            enrollments = Enrollment.objects.filter(course=course)
            if enrollments.count() == 0:
                continue
            avg = enrollments.aggregate(avg=Avg("progress"))["avg"] or 0
            top_courses.append({
                "code": course.code,
                "title": course.title,
                "students": enrollments.count(),
                "completed": enrollments.filter(completed=True).count(),
                "avg": round(avg),
            })
        top_courses = sorted(
            top_courses, key=lambda x: x["students"], reverse=True
        )[:10]

        recent_activity = LessonProgress.objects.select_related(
            "student__user", "lesson__module__course"
        ).order_by("-id")[:20]

        context = {
            **self.each_context(request),
            "title": "Student Activity",
            "total_students": total_students,
            "total_enrollments": total_enrollments,
            "total_completions": total_completions,
            "total_lessons_done": total_lessons_done,
            "overall_avg": overall_avg,
            "top_students": top_students,
            "top_courses": top_courses,
            "recent_activity": recent_activity,
        }
        return TemplateResponse(request, "admin/student_activity.html", context)


elec_admin = ELecturerAdminSite(name="elec_admin")


# =========================
# FACULTY
# =========================

class FacultyAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "faculty", "slug")
    list_filter = ("faculty",)
    search_fields = ("name",)


class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "department")
    list_filter = ("department",)
    search_fields = ("name",)


class LevelAdmin(admin.ModelAdmin):
    list_display = ("name",)


class SemesterAdmin(admin.ModelAdmin):
    list_display = ("name",)


# =========================
# COURSE
# =========================

class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "level", "semester", "total_enrollments", "avg_progress_display")
    list_filter = ("level", "semester")
    search_fields = ("code", "title")

    def total_enrollments(self, obj):
        count = Enrollment.objects.filter(course=obj).count()
        return format_html(
            '<span style="background:#e0f2fe;color:#0369a1;padding:3px 10px;'
            'border-radius:20px;font-weight:700;">👥 {}</span>',
            count
        )
    total_enrollments.short_description = "Students"

    def avg_progress_display(self, obj):
        avg = round(
            Enrollment.objects.filter(course=obj).aggregate(
                avg=Avg("progress")
            )["avg"] or 0
        )
        color = "#16a34a" if avg >= 70 else "#d97706" if avg >= 30 else "#dc2626"
        bg = "#f0fdf4" if avg >= 70 else "#fffbeb" if avg >= 30 else "#fef2f2"
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;'
            'border-radius:20px;font-weight:700;">{}%</span>',
            bg, color, avg
        )
    avg_progress_display.short_description = "Avg Progress"


# =========================
# PROGRAMME COURSE
# =========================

class ProgrammeCourseAdmin(admin.ModelAdmin):
    list_display = ("programme", "course")
    list_filter = ("programme",)


# =========================
# MODULE + LESSON
# =========================

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1
    fields = ("title", "order", "video_type", "video_url", "video_file", "description")
    ordering = ("order",)


class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")
    list_filter = ("course",)
    search_fields = ("title",)
    inlines = [LessonInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "order", "video_type", "completion_rate", "video_preview")
    list_filter = ("module", "video_type")
    search_fields = ("title",)
    readonly_fields = ("video_preview", "completion_stats")

    fieldsets = (
        ("Lesson Info", {
            "fields": ("module", "title", "order", "description"),
        }),
        ("Video Source", {
            "fields": ("video_type", "video_url", "video_file", "video_preview"),
        }),
        ("Student Activity", {
            "fields": ("completion_stats",),
        }),
    )

    def completion_rate(self, obj):
        total = LessonProgress.objects.filter(lesson=obj).count()
        completed = LessonProgress.objects.filter(lesson=obj, is_completed=True).count()
        if total == 0:
            return format_html('<span style="color:#9ca3af;">No data</span>')
        rate = int((completed / total) * 100)
        color = "#16a34a" if rate >= 70 else "#d97706" if rate >= 30 else "#dc2626"
        bg = "#f0fdf4" if rate >= 70 else "#fffbeb" if rate >= 30 else "#fef2f2"
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;'
            'border-radius:20px;font-weight:700;">✅ {}% ({}/{})</span>',
            bg, color, rate, completed, total
        )
    completion_rate.short_description = "Completion Rate"

    def completion_stats(self, obj):
        total = LessonProgress.objects.filter(lesson=obj).count()
        completed = LessonProgress.objects.filter(lesson=obj, is_completed=True).count()
        return format_html(
            '<div style="padding:12px;background:#f8fafc;border-radius:10px;'
            'border:1px solid #e2e8f0;">'
            '<p style="margin:0 0 8px;font-weight:700;">📊 Student Activity</p>'
            '<p style="margin:4px 0;">👁️ Total views: <strong>{}</strong></p>'
            '<p style="margin:4px 0;color:#16a34a;">✅ Completed: <strong>{}</strong></p>'
            '<p style="margin:4px 0;color:#dc2626;">⏳ Not completed: <strong>{}</strong></p>'
            '</div>',
            total, completed, total - completed
        )
    completion_stats.short_description = "Activity Stats"

    def video_preview(self, obj):
        try:
            video = obj.get_video()
        except Exception:
            return "No video"
        if not video:
            return "No video added yet"
        if obj.video_type == "url":
            if "youtube.com" in video or "youtu.be" in video:
                if "watch?v=" in video:
                    video_id = video.split("watch?v=")[-1].split("&")[0]
                elif "youtu.be/" in video:
                    video_id = video.split("youtu.be/")[-1].split("?")[0]
                else:
                    video_id = None
                if video_id:
                    return format_html(
                        '<iframe width="480" height="270" src="https://www.youtube.com/embed/{}" '
                        'frameborder="0" allowfullscreen style="border-radius:8px;"></iframe>',
                        video_id
                    )
            return format_html('<a href="{}" target="_blank" style="color:#38bdf8;">▶ Open Link</a>', video)
        if obj.video_type == "file":
            return format_html(
                '<video width="480" height="270" controls style="border-radius:8px;">'
                '<source src="{}">Your browser does not support video.</video>',
                video
            )
        return "No video"
    video_preview.short_description = "Video Preview"


# =========================
# COURSE Q&A ADMIN
# =========================

class CourseQAAdmin(admin.ModelAdmin):
    list_display = (
        "title", "course", "content_type",
        "is_published", "order", "created_at",
        "preview_link", "download_link"
    )
    list_filter = ("content_type", "is_published", "course")
    search_fields = ("title", "course__code", "course__title")
    ordering = ("course", "order", "-created_at")

    fieldsets = (
        ("Basic Info", {
            "fields": ("course", "content_type", "title", "order", "is_published"),
        }),
        ("Content", {
            "description": "Paste your questions & answers or summary text below.",
            "fields": ("content",),
        }),
    )

    def preview_link(self, obj):
        return format_html(
            '<a href="/course/{}/qa/" target="_blank" '
            'style="background:#e0f2fe;color:#0369a1;padding:4px 10px;'
            'border-radius:8px;font-weight:600;text-decoration:none;">👁 Preview</a>',
            obj.course.id
        )
    preview_link.short_description = "Student View"

    def download_link(self, obj):
        return format_html(
            '<a href="/admin/core/courseqa/{}/download/" '
            'style="background:#f0fdf4;color:#16a34a;padding:4px 10px;'
            'border-radius:8px;font-weight:600;text-decoration:none;">📄 PDF</a>',
            obj.id
        )
    download_link.short_description = "Download"

    def get_urls(self):
        urls = super().get_urls()
        custom = [
            path(
                '<int:qa_id>/download/',
                self.admin_site.admin_view(self.download_pdf),
                name='courseqa_download_pdf'
            ),
        ]
        return custom + urls

    def download_pdf(self, request, qa_id):
        qa = CourseQA.objects.get(id=qa_id)

        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.lib.units import cm
            from reportlab.lib import colors
            from reportlab.platypus import (
                SimpleDocTemplate, Paragraph, Spacer,
                HRFlowable, Table, TableStyle
            )

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=2*cm,
                leftMargin=2*cm,
                topMargin=2*cm,
                bottomMargin=2*cm
            )

            styles = getSampleStyleSheet()
            story = []

            # Header
            header_style = ParagraphStyle(
                'Header',
                parent=styles['Heading1'],
                fontSize=18,
                textColor=colors.HexColor('#0f172a'),
                spaceAfter=6,
            )
            sub_style = ParagraphStyle(
                'Sub',
                parent=styles['Normal'],
                fontSize=11,
                textColor=colors.HexColor('#64748b'),
                spaceAfter=4,
            )
            body_style = ParagraphStyle(
                'Body',
                parent=styles['Normal'],
                fontSize=11,
                leading=16,
                textColor=colors.HexColor('#1e293b'),
                spaceAfter=8,
            )

            story.append(Paragraph(f"E-Lecturer", sub_style))
            story.append(Paragraph(qa.title, header_style))
            story.append(Paragraph(
                f"Course: {qa.course.code} — {qa.course.title}  |  "
                f"Type: {qa.get_content_type_display()}",
                sub_style
            ))
            story.append(HRFlowable(
                width="100%", thickness=1,
                color=colors.HexColor('#e2e8f0'),
                spaceAfter=16
            ))

            # Content — split by lines
            for line in qa.content.split('\n'):
                line = line.strip()
                if not line:
                    story.append(Spacer(1, 6))
                    continue
                if line.startswith('Q:') or line.startswith('Question:'):
                    q_style = ParagraphStyle(
                        'Q',
                        parent=styles['Normal'],
                        fontSize=12,
                        fontName='Helvetica-Bold',
                        textColor=colors.HexColor('#0f172a'),
                        spaceAfter=4,
                        spaceBefore=12,
                    )
                    story.append(Paragraph(line, q_style))
                elif line.startswith('A:') or line.startswith('Answer:'):
                    a_style = ParagraphStyle(
                        'A',
                        parent=styles['Normal'],
                        fontSize=11,
                        textColor=colors.HexColor('#16a34a'),
                        spaceAfter=8,
                        leftIndent=20,
                    )
                    story.append(Paragraph(line, a_style))
                else:
                    story.append(Paragraph(line, body_style))

            doc.build(story)
            buffer.seek(0)

            filename = f"{qa.course.code}_{qa.title.replace(' ', '_')}.pdf"
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

        except ImportError:
            # Fallback: plain text download if reportlab not installed
            content = f"E-Lecturer\n{qa.title}\nCourse: {qa.course.code} — {qa.course.title}\n\n{qa.content}"
            response = HttpResponse(content, content_type='text/plain')
            filename = f"{qa.course.code}_{qa.title.replace(' ', '_')}.txt"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response


# =========================
# STUDENT PROFILE
# =========================

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "email_display", "total_courses", "completed_courses", "avg_progress_display", "total_lessons_done")
    search_fields = ("user__username", "user__email", "user__first_name")

    def email_display(self, obj):
        return obj.user.email
    email_display.short_description = "Email"

    def total_courses(self, obj):
        count = Enrollment.objects.filter(student=obj.user).count()
        return format_html(
            '<span style="background:#e0f2fe;color:#0369a1;padding:3px 10px;'
            'border-radius:20px;font-weight:700;">📚 {}</span>', count
        )
    total_courses.short_description = "Enrolled"

    def completed_courses(self, obj):
        count = Enrollment.objects.filter(student=obj.user, completed=True).count()
        color = "#16a34a" if count > 0 else "#6b7280"
        bg = "#f0fdf4" if count > 0 else "#f9fafb"
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;'
            'border-radius:20px;font-weight:700;">🏆 {}</span>',
            bg, color, count
        )
    completed_courses.short_description = "Completed"

    def avg_progress_display(self, obj):
        avg = round(
            Enrollment.objects.filter(student=obj.user).aggregate(
                avg=Avg("progress")
            )["avg"] or 0
        )
        color = "#16a34a" if avg >= 70 else "#d97706" if avg >= 30 else "#dc2626"
        bg = "#f0fdf4" if avg >= 70 else "#fffbeb" if avg >= 30 else "#fef2f2"
        return format_html(
            '<div style="display:flex;align-items:center;gap:8px;">'
            '<div style="width:80px;height:8px;background:#e5e7eb;border-radius:10px;overflow:hidden;">'
            '<div style="width:{}%;height:100%;background:{};border-radius:10px;"></div>'
            '</div>'
            '<span style="background:{};color:{};padding:3px 8px;'
            'border-radius:20px;font-weight:700;font-size:11px;">{}%</span>'
            '</div>',
            avg, color, bg, color, avg
        )
    avg_progress_display.short_description = "Avg Progress"

    def total_lessons_done(self, obj):
        count = LessonProgress.objects.filter(student=obj, is_completed=True).count()
        return format_html(
            '<span style="background:#fef3c7;color:#92400e;padding:3px 10px;'
            'border-radius:20px;font-weight:700;">✅ {} lessons</span>', count
        )
    total_lessons_done.short_description = "Lessons Done"


# =========================
# ENROLLMENT
# =========================

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student_name", "course", "progress_bar", "completed_badge", "enrolled_at", "hours_learned")
    list_filter = ("completed", "course__level", "course__semester")
    search_fields = ("student__username", "student__first_name", "course__code", "course__title")
    ordering = ("-enrolled_at",)

    def student_name(self, obj):
        initial = obj.student.first_name[0].upper() if obj.student.first_name else "S"
        return format_html(
            '<div style="display:flex;align-items:center;gap:8px;">'
            '<div style="width:30px;height:30px;border-radius:50%;'
            'background:linear-gradient(135deg,#00c2ff,#00f5d4);'
            'display:flex;align-items:center;justify-content:center;'
            'font-weight:800;font-size:12px;color:#0a0f1e;">{}</div>'
            '<div><div style="font-weight:600;font-size:13px;">{}</div>'
            '<div style="font-size:11px;color:#6b7280;">{}</div></div>'
            '</div>',
            initial,
            obj.student.first_name or obj.student.username,
            obj.student.email
        )
    student_name.short_description = "Student"

    def progress_bar(self, obj):
        progress = round(obj.progress)
        color = "#16a34a" if progress >= 70 else "#d97706" if progress >= 30 else "#3b82f6"
        return format_html(
            '<div style="display:flex;align-items:center;gap:8px;min-width:140px;">'
            '<div style="flex:1;height:8px;background:#e5e7eb;border-radius:10px;overflow:hidden;">'
            '<div style="width:{}%;height:100%;background:{};border-radius:10px;"></div>'
            '</div>'
            '<span style="font-size:12px;font-weight:700;color:{};min-width:32px;">{}%</span>'
            '</div>',
            progress, color, color, progress
        )
    progress_bar.short_description = "Progress"

    def completed_badge(self, obj):
        if obj.completed:
            return format_html(
                '<span style="background:#f0fdf4;color:#16a34a;padding:4px 12px;'
                'border-radius:20px;font-weight:700;font-size:12px;'
                'border:1px solid #bbf7d0;">✅ Completed</span>'
            )
        return format_html(
            '<span style="background:#fff7ed;color:#c2410c;padding:4px 12px;'
            'border-radius:20px;font-weight:700;font-size:12px;'
            'border:1px solid #fed7aa;">⏳ In Progress</span>'
        )
    completed_badge.short_description = "Status"


# =========================
# LESSON PROGRESS
# =========================

class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("student_name", "lesson_title", "course_name", "status_badge")
    list_filter = ("is_completed", "lesson__module__course")
    search_fields = ("student__user__username", "student__user__first_name", "lesson__title")
    ordering = ("-id",)

    def student_name(self, obj):
        return format_html(
            '<strong>{}</strong><br>'
            '<span style="font-size:11px;color:#6b7280;">{}</span>',
            obj.student.user.first_name or obj.student.user.username,
            obj.student.user.email
        )
    student_name.short_description = "Student"

    def lesson_title(self, obj):
        return obj.lesson.title
    lesson_title.short_description = "Lesson"

    def course_name(self, obj):
        return format_html(
            '<span style="background:#e0f2fe;color:#0369a1;padding:3px 8px;'
            'border-radius:6px;font-size:12px;font-weight:600;">{}</span>',
            obj.lesson.module.course.code
        )
    course_name.short_description = "Course"

    def status_badge(self, obj):
        if obj.is_completed:
            return format_html(
                '<span style="background:#f0fdf4;color:#16a34a;padding:4px 12px;'
                'border-radius:20px;font-weight:700;font-size:12px;">✅ Completed</span>'
            )
        return format_html(
            '<span style="background:#f9fafb;color:#6b7280;padding:4px 12px;'
            'border-radius:20px;font-weight:700;font-size:12px;">👁️ Viewed</span>'
        )
    status_badge.short_description = "Status"


# =========================
# REGISTER WITH BOTH SITES
# =========================

for site in [elec_admin, admin.site]:
    site.register(Faculty, FacultyAdmin)
    site.register(Department, DepartmentAdmin)
    site.register(Programme, ProgrammeAdmin)
    site.register(Level, LevelAdmin)
    site.register(Semester, SemesterAdmin)
    site.register(Course, CourseAdmin)
    site.register(ProgrammeCourse, ProgrammeCourseAdmin)
    site.register(CourseModule, CourseModuleAdmin)
    site.register(Lesson, LessonAdmin)
    site.register(StudentProfile, StudentProfileAdmin)
    site.register(Enrollment, EnrollmentAdmin)
    site.register(LessonProgress, LessonProgressAdmin)
    site.register(CourseQA, CourseQAAdmin)

elec_admin.register(User)