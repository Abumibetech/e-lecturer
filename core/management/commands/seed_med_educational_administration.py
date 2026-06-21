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
    help = "Seed M.Ed Educational Administration and Planning courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Educational Administration and Planning"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Ed. Educational Administration and Planning"
        )

        courses = {

            # =========================
            # 800 LEVEL FIRST SEMESTER
            # =========================
            (800, "First Semester"): [

                ("GST807", "The Good Study Guide"),
                ("EDA811", "Concepts and Theories of Educational Administration and Planning"),
                ("EDA812", "Practicum in Educational Management"),
                ("EDU821", "Statistical Methods"),
                ("EDU822", "Advanced Educational Psychology"),
                ("EDU823", "Educational Research Methods"),

                # Electives
                ("EDA821", "Human Resources Management in Education"),
                ("EDA825", "Managerial Psychology"),
                ("EDA831", "Project Management in Education"),
            ],

            # ==========================
            # 800 LEVEL SECOND SEMESTER
            # ==========================
            (800, "Second Semester"): [

                ("EDA823", "Seminar"),
                ("EDA832", "Economics of Education"),
                ("EDA833", "Monitoring and Evaluation in Educational Management"),
                ("EDA834", "Budgeting and Financial Management in Education"),
                ("EDA842", "Application of Management Information Systems in Education"),
                ("EDA844", "Educational Statistics for Education Managers"),
                ("EDA851", "Principles of Institutional Administration in Education"),
                ("EDA855", "Responsibility and Accountability Management in Education"),
                ("EDU820", "Research Project"),

                # Electives
                ("EDA813", "School Plant Management"),
                ("EDA822", "Supervision of Instruction in Education"),
                ("EDA852", "Politics of Education"),
                ("EDA854", "Legal Aspects of Educational Administration"),
                ("EDA856", "Problems and Issues in Higher Education"),
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
                "M.Ed Educational Administration and Planning courses seeded successfully."
            )
        )