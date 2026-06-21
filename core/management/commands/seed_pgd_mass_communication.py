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
    help = "Seed PGD Mass Communication courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Communication and Media Studies"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mass Communication"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Mass Communication"
        )

        courses = {

            (700, "First Semester"): [
                ("GST707", "The Good Study Guide"),
                ("CIT701", "Foundation of Information and Communication Technology"),
                ("JLS711", "Introduction to Journalism"),
                ("JLS713", "Media and Society"),
                ("JLS714", "Communication Research"),
                ("JLS721", "News Reporting and Writing"),
                ("FRE701", "Basic French Grammar I"),

                # Elective
                ("CSS755", "Patterns and Trends of Crime in Nigeria"),
            ],

            (700, "Second Semester"): [
                ("JLS712", "Media Law and Ethics"),
                ("JLS722", "Publication Layout and Design"),
                ("JLS724", "Feature Writing"),
                ("JLS726", "Speech Writing"),
                ("JLS742", "Fundamentals of Broadcasting"),

                # Electives
                ("JLS732", "Principles and Practice of Public Relations"),
                ("FRE702", "Basic French Grammar and Composition II"),
            ],

            (700, "Project"): [
                ("JLS716", "Professional Project / Long Essay"),
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
                "PGD Mass Communication courses seeded successfully."
            )
        )