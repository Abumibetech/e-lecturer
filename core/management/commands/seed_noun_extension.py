from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Seed Agricultural Extension & Rural Development ONLY"

    def handle(self, *args, **kwargs):

        # =========================
        # LEVELS
        # =========================
        levels = {}
        for i in range(100, 600, 100):
            levels[i], _ = Level.objects.get_or_create(name=i)

        # =========================
        # SEMESTERS
        # =========================
        sem1, _ = Semester.objects.get_or_create(name="First Semester")
        sem2, _ = Semester.objects.get_or_create(name="Second Semester")

        # =========================
        # FACULTY
        # =========================
        faculty_name = "FACULTY OF AGRICULTURAL SCIENCES"
        faculty, _ = Faculty.objects.get_or_create(
            slug=slugify(faculty_name),
            defaults={"name": faculty_name}
        )

        # =========================
        # DEPARTMENT
        # =========================
        dept_name = "Department of Agricultural Economics and Extension"
        department, _ = Department.objects.get_or_create(
            slug=slugify(dept_name),
            faculty=faculty,
            defaults={"name": dept_name}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme_name = "B.Sc Agricultural Extension and Rural Development"
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name=programme_name
        )

        # =========================
        # COURSES (FULL STRUCTURE EXAMPLE)
        # =========================
        courses = [
            # 100 level
            (100, sem1, "AER101", "Introduction to Agricultural Extension"),
            (100, sem2, "AER102", "Rural Sociology and Development"),

            # 200 level
            (200, sem1, "AER201", "Extension Communication Methods"),
            (200, sem2, "AER202", "Farm Management Principles"),

            # 300 level
            (300, sem1, "AER301", "Agricultural Development Policies"),
            (300, sem2, "AER302", "Community Development Practice"),

            # 400 level
            (400, sem1, "AER401", "Advanced Extension Strategies"),
            (400, sem2, "AER402", "Project Research / Final Year Project"),
        ]

        created = 0

        for level, semester, code, title in courses:
            Course.objects.get_or_create(
                programme=programme,
                level=levels[level],
                semester=semester,
                code=code,
                defaults={"title": title}
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f"✔ Agricultural Extension seed completed → {created} courses"
        ))