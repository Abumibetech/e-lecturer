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
    help = "Seed PGD Economics courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Economics"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Economics"
        )

        courses = {

            ("PGD", "First Semester"): [
                ("ECO711", "Advanced Principles of Economics"),
                ("ECO712", "Mathematics for Economists"),
                ("ECO713", "Statistics for Economists"),
                ("ECO714", "Computer Applications for Economists"),
                ("ECO715", "Development Economics"),
                ("ECO716", "Financial Economics"),
            ],

            ("PGD", "Second Semester"): [
                ("ECO721", "Structure of the Nigerian Economy"),
                ("ECO722", "Introduction to Econometrics"),
                ("ECO723", "Public Sector Economics"),
                ("ECO724", "Monetary Economics"),
                ("ECO725", "International Economics"),
                ("ECO726", "Research Methodology"),
                ("ECO790", "Research Project"),
            ],
        }

        for (level_name, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=level_name
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
                "PGD Economics courses seeded successfully."
            )
        )