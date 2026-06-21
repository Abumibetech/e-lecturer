# e_lecturer/celery.py
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_lecturer.settings')

app = Celery('e_lecturer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# ── Scheduled push notification tasks ──────────────────────
app.conf.beat_schedule = {

    # Daily study reminder — 8:00 AM Lagos time every day
    'daily-study-reminder': {
        'task':     'core.tasks.send_daily_study_reminder',
        'schedule': crontab(hour=8, minute=0),
    },

    # Check for course milestones every hour
    'check-course-milestones': {
        'task':     'core.tasks.check_course_milestones',
        'schedule': crontab(minute=0),
    },
}

app.conf.timezone = 'Africa/Lagos'
