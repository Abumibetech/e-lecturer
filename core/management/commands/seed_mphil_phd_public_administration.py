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
    help = "Seed M.Phil/PhD Public Administration courses"

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
            name="M.Phil/PhD Public Administration"
        )

        courses = {

            # =========================
            # 900 LEVEL FIRST SEMESTER
            # =========================
            (900, "First Semester"): [
                ("PUB905", "Advanced Development Administration Theory"),
                ("PUB907", "Advanced Research Methodology"),
            ],

            # =========================
            # 900 LEVEL SECOND SEMESTER
            # =========================
            (900, "Second Semester"): [
                ("PUB910", "Public Policy Analysis"),
                ("PUB912", "Inter-Governmental Relations"),
            ],

            # =========================
            # PHD RESEARCH STAGE (treated as 900 level)
            # =========================
            (900, "PhD Research Stage"): [
                ("PHD901", "PhD Seminar I"),
                ("PHD902", "PhD Seminar II"),
                ("PHD990", "Thesis / Dissertation"),
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
                "M.Phil/PhD Public Administration courses seeded successfully."
            )
        )