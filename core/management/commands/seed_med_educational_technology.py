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
    help = "Seed M.Ed Educational Technology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Educational Technology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Ed. Educational Technology"
        )

        courses = {

            # =========================
            # 800 LEVEL FIRST SEMESTER
            # =========================
            (800, "First Semester"): [

                ("GST807", "The Good Study Guide"),
                ("EDU821", "Statistical Methods"),
                ("EDU823", "Educational Research Methods"),
                ("EDT831", "Instructional Media Design and Production"),

                # Electives
                ("CIT753", "Introduction to Internet"),
                ("CIT759", "Micro Computing and WWW"),
                ("EDT821", "Instructional Task Analysis and Psychological Basis of Instruction"),
            ],

            # ==========================
            # 800 LEVEL SECOND SEMESTER
            # ==========================
            (800, "Second Semester"): [

                ("EDU820", "Research Project"),
                ("EDU822", "Advanced Educational Psychology"),
                ("EDT812", "Management of Educational Resources Centres"),
                ("EDT823", "Research and Media (Seminar)"),
                ("EDT830", "Multimedia Technology in Teaching and Learning"),
                ("EDT832", "Preparation, Utilization and Integration of Curriculum and Media"),
                ("EDT834", "Instructional Radio and Television"),
                ("EDA842", "Application of Management Information Systems in Education"),

                # Electives
                ("EDT811", "Theories of Communication and Philosophical Basis of Instructional Media"),
                ("EDT833", "Facilities for Media"),
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
                "M.Ed Educational Technology courses seeded successfully."
            )
        )