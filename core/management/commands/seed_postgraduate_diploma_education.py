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
    help = "Seed Postgraduate Diploma in Education (PGDE) courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Postgraduate Diploma in Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Postgraduate Diploma in Education (PGDE)"
        )

        courses = {

            # =========================
            # 700 LEVEL FIRST SEMESTER
            # =========================
            (700, "First Semester"): [

                ("GST707", "The Good Study Guide"),
                ("EDU712", "Professionalism in Teaching"),
                ("EDU716", "Sociology of Education"),
                ("EDU721", "Psychology of Learning"),
                ("EDU724", "Guidance and Counselling"),
                ("EDU726", "Measurement and Evaluation"),
                ("EDU740", "Mathematics Methods"),
                ("CIT726", "Computers in Society"),
            ],

            # ==========================
            # 700 LEVEL SECOND SEMESTER
            # ==========================
            (700, "Second Semester"): [

                ("EDU766", "Political Science Methods"),
            ],

            # =========================
            # 700 LEVEL THIRD SEMESTER
            # =========================
            (700, "Third Semester"): [

                ("EDU735", "Teaching Practice"),
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
                "PGDE courses seeded successfully."
            )
        )