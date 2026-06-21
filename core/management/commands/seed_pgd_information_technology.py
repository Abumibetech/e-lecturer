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
    help = "Seed PGD Information Technology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Computing"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Information Technology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Information Technology"
        )

        courses = {

            (700, "First Semester"): [
                ("GST707", "A Study Guide for the Distance Learner"),
                ("CIT701", "Foundation of Information and Communication Technology"),
                ("CIT703", "Information Technology and Software Development"),
                ("CIT753", "Introduction to Internet"),
                ("CIT735", "Application Software Design and Multimedia"),

                # Electives
                ("CIT711", "Computer Fundamentals"),
                ("CIT759", "Micro Computing and WWW"),
                ("CIT721", "Information System Design and Programming"),
            ],

            (700, "Second Semester"): [
                ("CIT722", "Computer Networks"),
                ("CIT736", "Computer Programming"),
                ("CIT756", "Operations Research"),
                ("CIT752", "Operating System Concepts"),
                ("CIT799", "Project"),

                # Electives
                ("CIT734", "Object-Oriented Technology"),
                ("CIT742", "Multimedia Technology"),
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
                "PGD Information Technology courses seeded successfully."
            )
        )