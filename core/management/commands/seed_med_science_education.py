from django.core.management.base import BaseCommand
from core.models import (
    Faculty,
    Department,
    Programme,
    Level,
    Semester,
    Course,
)


class Command(BaseCommand):
    help = "Seed M.Ed. Science Education"

    def handle(self, *args, **kwargs):

        # Faculty
        faculty, _ = Faculty.objects.get_or_create(
            name="Education",
            defaults={"slug": "education"}
        )

        # Department
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Science Education",
            defaults={"slug": "science-education"}
        )

        # Programme
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Ed. Science Education"
        )

        # Level
        level, _ = Level.objects.get_or_create(name=800)

        # Semesters
        first_semester, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        second_semester, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        courses = [

            # Research Methods
            ("EDU823", "Research Methods", first_semester),

            # Statistics
            ("EDU821", "Statistics", first_semester),

            # Educational Psychology
            ("EDU822", "Educational Psychology", first_semester),

            # Graduate Seminar
            ("SED800", "Graduate Seminar", first_semester),

            # Science Education Core
            ("SED811", "Science Education Core I", first_semester),
            ("SED831", "Science Education Core II", first_semester),
            ("SED832", "Science Education Core III", second_semester),
            ("SED834", "Science Education Core IV", second_semester),
            ("SED835", "Science Education Core V", second_semester),

            # Educational Technology
            ("EDT830", "Educational Technology I", first_semester),
            ("EDT831", "Educational Technology II", second_semester),

            # Management Information Systems
            ("EDA842", "Management Information Systems", second_semester),

            # Research Project
            ("EDU820", "Research Project", second_semester),
        ]

        created = 0

        for code, title, semester in courses:

            _, was_created = Course.objects.get_or_create(
                programme=programme,
                level=level,
                semester=semester,
                code=code,
                defaults={
                    "title": title,
                    "description": title,
                }
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {created} M.Ed. Science Education courses"
            )
        )