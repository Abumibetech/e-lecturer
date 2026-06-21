from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        unique_together = ("faculty", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Programme(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name} Level"


class Semester(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    code        = models.CharField(max_length=20, unique=True)
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    level       = models.ForeignKey(Level, on_delete=models.CASCADE)
    semester    = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.title}"


class ProgrammeCourse(models.Model):
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE)
    course    = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("programme", "course")

    def __str__(self):
        return f"{self.programme.name} - {self.course.code}"


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title  = models.CharField(max_length=255)
    order  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Lesson(models.Model):
    VIDEO_TYPE_URL  = "url"
    VIDEO_TYPE_FILE = "file"
    VIDEO_TYPE_CHOICES = [
        (VIDEO_TYPE_URL,  "Video URL (YouTube / external link)"),
        (VIDEO_TYPE_FILE, "Upload Video File"),
    ]

    module     = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name="lessons")
    title      = models.CharField(max_length=255)
    order      = models.PositiveIntegerField(default=0)
    video_type = models.CharField(max_length=10, choices=VIDEO_TYPE_CHOICES, default=VIDEO_TYPE_URL)
    video_url  = models.URLField(blank=True, null=True, help_text="Paste YouTube or any video URL here")
    video_file = models.FileField(
        upload_to="lessons/videos/", blank=True, null=True,
        help_text="Upload an MP4, MOV, or AVI video file"
    )
    description = models.TextField(blank=True, null=True, help_text="Optional lesson notes or description")

    class Meta:
        ordering = ["order"]

    def get_video(self):
        if self.video_type == self.VIDEO_TYPE_FILE and self.video_file:
            return self.video_file.url
        if self.video_type == self.VIDEO_TYPE_URL and self.video_url:
            return self.video_url
        return None

    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Enrollment(models.Model):
    student              = models.ForeignKey(User, on_delete=models.CASCADE)
    course               = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress             = models.FloatField(default=0)
    completed            = models.BooleanField(default=False)
    hours_learned        = models.FloatField(default=0)
    enrolled_at          = models.DateTimeField(auto_now_add=True)
    notified_milestones  = models.JSONField(default=list, blank=True)

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student.username} - {self.course.code}"


class LessonProgress(models.Model):
    student       = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    lesson        = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed  = models.BooleanField(default=False)
    last_position = models.FloatField(default=0, help_text="Video resume position in seconds")

    class Meta:
        unique_together = ("student", "lesson")

    def __str__(self):
        return f"{self.student.user.username} - {self.lesson.title}"


class CourseQA(models.Model):
    TYPE_CHOICES = [
        ("summary", "Summary / Notes"),
        ("qa",      "Questions & Answers"),
    ]

    course       = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="qa_items")
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="qa")
    title        = models.CharField(max_length=255, help_text="e.g. Week 3 Q&A or Midterm Summary")
    content      = models.TextField(help_text="Paste your questions/answers or summary text here")
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.course.code} — {self.title}"


class PushSubscription(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="push_subscriptions")
    endpoint   = models.TextField(unique=True)
    p256dh     = models.TextField()
    auth       = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name        = "Push Subscription"
        verbose_name_plural = "Push Subscriptions"

    def __str__(self):
        return f"{self.user.username} — {self.endpoint[:60]}..."