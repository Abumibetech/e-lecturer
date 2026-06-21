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
    help = "Seed PGD Public Administration courses"

    def handle(self, *args, **kwargs):

        # Use existing Faculty of Social Sciences if it exists
        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Public Administration"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Public Administration"
        )

        courses = {

            # =========================
            # 700 LEVEL FIRST SEMESTER
            # =========================
            (700, "First Semester"): [
                ("GST707", "The Good Study Guide"),
                ("CIT705", "Computer Applications in Business"),
                ("PAD707", "Local Government Administration"),
                ("BUS727", "Organisational Behaviour"),
                ("FMS731", "Research Methodology"),
                ("PUL743", "Administrative Law"),
                ("PAD747", "Introduction to Public Administration"),
                ("PAD771", "Public Personnel Administration"),
                ("BFN779", "Public Financial Management"),

                # Elective
                ("BFN715", "Principles of Finance"),
                ("ACC757", "Principles of Accounting"),
            ],

            # =========================
            # 700 LEVEL SECOND SEMESTER
            # =========================
            (700, "Second Semester"): [
                ("PAD710", "Public Policy Analysis"),
                ("PAD712", "Administrative Theory"),
                ("PAD724", "Public Enterprises Management"),
                ("PAD742", "Development Theory and Administration"),
                ("PAD756", "Project Analysis and Implementation"),
                ("PAD784", "Comparative Public Administration"),
                ("PAD790", "Research Project"),

                # Elective
                ("BUS726", "Global Economic Environment"),
                ("BUS714", "Principles of Management"),
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
                "PGD Public Administration courses seeded successfully."
            )
        )