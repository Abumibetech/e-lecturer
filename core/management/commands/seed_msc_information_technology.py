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
    help = "Seed M.Sc. Information Technology courses"

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
            name="M.Sc. Information Technology"
        )

        courses = {

            (800, "First Semester"): [
                ("GST807", "A Study Guide for the Distance Learner"),
                ("CIT843", "Introduction to Database Management Systems"),
                ("CIT831", "Software Engineering Methodologies"),
                ("CIT853", "Internet Concepts and Web Design"),
                ("CIT851", "Advanced Systems Analysis and Design"),

                # Electives
                ("CIT841", "Advanced Information Storage and Retrieval"),
                ("CIT811", "User Interface Design and Ergonomics"),
                ("CIT855", "Advanced Cyber Security"),
                ("CIT891", "Advanced Multimedia Technology"),
            ],

            (800, "Second Semester"): [
                ("CIT802", "Technical Report Writing"),
                ("CIT854", "Network Design and Programming"),
                ("CIT852", "Data Communication and Networks"),
                ("CIT834", "Object-Oriented Programming Using C#"),
                ("CIT803", "Seminar on Emerging Technologies"),

                # Electives
                ("CIT832", "Operating Systems Concepts and Networking"),
                ("CIT844", "Advanced Database Management Systems"),
                ("CIT882", "Internet of Things"),
            ],

            (800, "Third Semester"): [
                ("CIT899", "Research Project"),
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
                "M.Sc. Information Technology courses seeded successfully."
            )
        )