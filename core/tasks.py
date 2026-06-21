# core/tasks.py
import json
import logging
from celery import shared_task
from django.conf import settings

logger = logging.getLogger(__name__)


# ── Internal helper ──────────────────────────────────────────

def _send_push(subscription, title, body, icon="/static/icons/icon-192.png", url="/dashboard/"):
    """Send one Web Push notification. Returns True on success."""
    try:
        from pywebpush import webpush, WebPushException

        webpush(
            subscription_info={
                "endpoint": subscription.endpoint,
                "keys": {"p256dh": subscription.p256dh, "auth": subscription.auth},
            },
            data=json.dumps({"title": title, "body": body, "icon": icon, "url": url}),
            vapid_private_key=settings.VAPID_PRIVATE_KEY,
            vapid_claims={"sub": settings.VAPID_CLAIMS_EMAIL},
        )
        return True

    except Exception as e:
        logger.warning(f"Push failed: {e}")
        # Subscription is gone — clean it up
        if hasattr(e, 'response') and e.response and e.response.status_code in (404, 410):
            subscription.delete()
        return False


# ── Task 1: Daily study reminder ─────────────────────────────

@shared_task(name="core.tasks.send_daily_study_reminder")
def send_daily_study_reminder():
    """
    Fires every day at 8:00 AM Lagos time (configured in celery.py).
    Sends a personalised nudge to every student with at least one
    incomplete enrolled course.
    """
    from .models import PushSubscription, Enrollment

    active_ids = Enrollment.objects.filter(
        completed=False
    ).values_list('student_id', flat=True).distinct()

    subscriptions = PushSubscription.objects.filter(
        user_id__in=active_ids
    ).select_related('user')

    sent = 0
    for sub in subscriptions:
        name       = sub.user.first_name or sub.user.username
        incomplete = Enrollment.objects.filter(student=sub.user, completed=False).count()
        body       = (
            f"Hi {name}! 📚 You have {incomplete} course"
            f"{'s' if incomplete > 1 else ''} in progress. "
            f"Keep going — consistency is key!"
        )
        if _send_push(sub, title="⏰ Daily Study Reminder", body=body, url="/my-courses/"):
            sent += 1

    logger.info(f"Daily reminder sent to {sent} students.")
    return f"Sent to {sent} students"


# ── Task 2: Milestone checker ────────────────────────────────

@shared_task(name="core.tasks.check_course_milestones")
def check_course_milestones():
    """
    Runs every hour. Sends a notification when a student crosses
    a 25 / 50 / 75 / 100% milestone for the first time.
    Uses Enrollment.notified_milestones (JSONField) to avoid repeats.
    """
    from .models import PushSubscription, Enrollment

    MILESTONES = [25, 50, 75, 100]

    enrollments = Enrollment.objects.select_related(
        'student', 'course'
    ).filter(student__push_subscriptions__isnull=False).distinct()

    sent = 0
    for enrollment in enrollments:
        progress  = round(enrollment.progress)
        course    = enrollment.course
        student   = enrollment.student
        notified  = enrollment.notified_milestones or []
        changed   = False

        for milestone in MILESTONES:
            if progress >= milestone and milestone not in notified:
                subs = PushSubscription.objects.filter(user=student)

                if milestone == 100:
                    title = "🎉 Course Completed!"
                    body  = f"Amazing! You finished {course.code} — {course.title}. Well done!"
                    url   = "/my-courses/"
                else:
                    title = f"🏆 {milestone}% Milestone!"
                    body  = f"You're {milestone}% through {course.code}. Keep pushing!"
                    url   = f"/course/{course.id}/learn/"

                for sub in subs:
                    if _send_push(sub, title=title, body=body, url=url):
                        sent += 1

                notified.append(milestone)
                changed = True

        if changed:
            enrollment.notified_milestones = notified
            enrollment.save(update_fields=['notified_milestones'])

    logger.info(f"Milestone notifications sent: {sent}")
    return f"Milestone pushes: {sent}"
