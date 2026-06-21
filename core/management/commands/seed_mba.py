from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed MBA Programme"

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
            name="MBA"
        )

        # =========================
        # LEVEL
        # =========================
        level, _ = Level.objects.get_or_create(name=800)

        # =========================
        # SEMESTERS
        # =========================
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # =========================
            # FIRST SEMESTER
            # =========================
            (800, first_semester, "GST807", "Research Methodology and Academic Writing (Postgraduate Core)"),
            (800, first_semester, "MBA801", "Managerial Economics"),
            (800, first_semester, "MBA803", "Financial Management"),
            (800, first_semester, "MBA805", "Quantitative Methods for Management Decisions"),
            (800, first_semester, "MBA807", "Organizational Behaviour and Management Theory"),
            (800, first_semester, "MBA809", "Marketing Management"),
            (800, first_semester, "MBA811", "Accounting for Managers"),

            # =========================
            # SECOND SEMESTER
            # =========================
            (800, second_semester, "MBA802", "Strategic Management"),
            (800, second_semester, "MBA804", "Human Resource Management"),
            (800, second_semester, "MBA806", "Operations and Production Management"),
            (800, second_semester, "MBA808", "Business Ethics and Corporate Governance"),
            (800, second_semester, "MBA810", "Management Information Systems"),
            (800, second_semester, "MBA812", "Entrepreneurship and Innovation Management"),
            (800, second_semester, "MBA814", "Business Policy and Decision Making"),

            # =========================
            # ELECTIVES
            # =========================
            (800, first_semester, "MBA815", "International Business Management"),
            (800, first_semester, "MBA817", "Project Management"),
            (800, first_semester, "MBA819", "Supply Chain and Logistics Management"),
            (800, first_semester, "MBA821", "Public Sector Management"),
            (800, first_semester, "MBA823", "Small Business and Family Business Management"),
            (800, first_semester, "MBA825", "Leadership and Change Management"),

            # =========================
            # RESEARCH COMPONENT
            # =========================
            (800, second_semester, "MBA899", "MBA Dissertation / Research Project"),
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
                f"Successfully seeded {created} MBA courses"
            )
        )