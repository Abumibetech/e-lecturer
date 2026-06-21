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
    help = "Seed MPA (Master of Public Administration) courses"

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
            name="MPA (Master of Public Administration)"
        )

        courses = {

            # =========================
            # 800 LEVEL FIRST SEMESTER
            # =========================
            (800, "First Semester"): [
                ("GST807", "The Good Study Guide"),
                ("PAD851", "Organizational Behaviour and Theory"),
                ("PAD852", "Public Personnel Management"),
                ("PAD853", "E-Governance in the Public Sector"),
                ("FMS805", "Research Methodology"),

                # Electives
                ("MPA853", "International Administration"),
                ("BUS847", "Global Economic Environment"),
            ],

            # =========================
            # 800 LEVEL SECOND SEMESTER
            # =========================
            (800, "Second Semester"): [
                ("PAD861", "Public Policy Analysis"),
                ("PAD862", "Administrative Theory"),
                ("PAD863", "Development Administration"),
                ("PAD864", "Public Enterprises Management"),
                ("PAD865", "Project Analysis and Implementation"),
                ("PAD866", "Comparative Public Administration"),

                # Electives
                ("PAD867", "Public Financial Management"),
                ("PAD868", "Intergovernmental Relations"),
            ],

            # =========================
            # 800 LEVEL THIRD SEMESTER
            # =========================
            (800, "Third Semester"): [
                ("PAD871", "Public Sector Strategic Management"),
                ("PAD872", "Governance and Public Sector Reform"),
                ("PAD873", "Public Budgeting and Fiscal Administration"),
                ("PAD874", "Administrative Law and Ethics"),
            ],

            # =========================
            # 800 LEVEL FOURTH SEMESTER
            # =========================
            (800, "Fourth Semester"): [
                ("PAD899", "Thesis / Dissertation"),
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
                "MPA (Master of Public Administration) courses seeded successfully."
            )
        )