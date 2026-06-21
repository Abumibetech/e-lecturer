from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed PGD Business Administration Programme"

    def handle(self, *args, **kwargs):

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Management Sciences",
            defaults={"slug": "management-sciences"}
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Business Administration",
            defaults={"slug": "business-administration"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Business Administration"
        )

        # =========================
        # LEVEL
        # =========================
        level, _ = Level.objects.get_or_create(name=700)

        # =========================
        # SEMESTERS
        # =========================
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # =========================
            # FIRST SEMESTER
            # =========================
            (700, first_semester, "GST701", "Study Skills and Research Methods (Postgraduate)"),
            (700, first_semester, "PGB701", "Principles of Management"),
            (700, first_semester, "PGB703", "Managerial Economics"),
            (700, first_semester, "PGB705", "Quantitative Methods for Business Decisions"),
            (700, first_semester, "PGB707", "Financial Accounting for Managers"),
            (700, first_semester, "PGB709", "Organizational Behaviour"),
            (700, first_semester, "PGB711", "Marketing Management Principles"),

            # =========================
            # SECOND SEMESTER
            # =========================
            (700, second_semester, "PGB702", "Strategic Management Fundamentals"),
            (700, second_semester, "PGB704", "Human Resource Management"),
            (700, second_semester, "PGB706", "Operations and Production Management"),
            (700, second_semester, "PGB708", "Business Law and Ethics"),
            (700, second_semester, "PGB710", "Entrepreneurship Development"),
            (700, second_semester, "PGB712", "Management Information Systems"),
            (700, second_semester, "PGB714", "Research Methods in Business Administration"),

            # =========================
            # ELECTIVES
            # =========================
            (700, first_semester, "PGB715", "International Business Management"),
            (700, first_semester, "PGB717", "Public Sector Management"),
            (700, first_semester, "PGB719", "Project Management Principles"),
            (700, first_semester, "PGB721", "Small Business Development and Management"),
            (700, first_semester, "PGB723", "Corporate Governance and Leadership"),

            # =========================
            # RESEARCH COMPONENT
            # =========================
            (700, second_semester, "PGB799", "Research Project / Long Essay"),
        ]

        created = 0

        for level_num, semester, code, title in courses:
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
                f"Successfully seeded {created} PGD Business Administration courses"
            )
        )