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
    help = "Seed M.Sc. Public Administration courses"

    def handle(self, *args, **kwargs):

        # Use existing Faculty of Social Sciences
        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Public Administration"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Sc. Public Administration"
        )

        courses = {

            # =========================
            # 800 LEVEL FIRST SEMESTER
            # =========================
            (800, "First Semester"): [
                ("GST807", "The Good Study Guide"),
                ("PAD813", "Quantitative Methods for Public Administration"),
                ("FMS825", "Research Methodology"),
                ("BUS831", "Organizational Behaviour and Theory"),
                ("BUS847", "Global Economic Environment"),

                # Electives
                ("PAD843", "E-Governance in the Public Sector"),
                ("PAD853", "International Administration"),
                ("PAD871", "Public Personnel Management"),
            ],

            # =========================
            # 800 LEVEL SECOND SEMESTER
            # =========================
            (800, "Second Semester"): [
                ("PAD821", "Theory and Practice of Public Administration"),
                ("PAD823", "Public Policy Analysis"),
                ("PAD825", "Comparative Public Administration"),
                ("PAD827", "Human Resource Management in the Public Sector"),
                ("PAD829", "Public Financial Management"),

                # Electives
                ("PAD831", "Development Administration"),
                ("PAD833", "Administrative Law and Public Service Ethics"),
                ("PAD835", "Strategic Management in the Public Sector"),
            ],

            # =========================
            # 800 LEVEL THIRD SEMESTER
            # =========================
            (800, "Third Semester"): [
                ("PAD841", "Local Government Administration"),
                ("PAD845", "International Relations and Diplomacy"),

                # Electives
                ("PAD847", "Leadership in the Public Sector"),
                ("PAD849", "Conflict Resolution and Peace Building"),
                ("PAD851", "Disaster Management and Humanitarian Response"),
                ("PAD855", "Advanced Public Sector Governance"),
            ],

            # =========================
            # 800 LEVEL FOURTH SEMESTER
            # =========================
            (800, "Fourth Semester"): [
                ("PAD899", "Dissertation"),
            ],
        }

        for (level_number, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=level_number
            )

            semester, _ = Semester.objects.get_or_create(
                name=semester_name
            )

            for code, title in course_list:

                Course.objects.get_or_create(
                    programme=programme,
                    code=code,
                    defaults={
                        "title": title,
                        "level": level,
                        "semester": semester,
                    }
                )

        self.stdout.write(
            self.style.SUCCESS(
                "M.Sc. Public Administration courses seeded successfully."
            )
        )