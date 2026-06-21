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
    help = "Seed PGD Peace Studies and Conflict Resolution courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Peace Studies and Conflict Resolution"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="PGD Peace Studies and Conflict Resolution"
        )

        courses = {

            (700, "First Semester"): [
                ("GST707", "The Good Study Guide"),
                ("CIT701", "Foundation of Information and Communication Technology"),
                ("PCR711", "Introduction to Peace Studies"),
                ("PCR713", "Introduction to Peace Education"),
                ("PCR715", "Introduction to Conflict Resolution Processes I"),
                ("PCR771", "Third Party Intervention in Conflict Resolution"),

                # Electives
                ("CRS702", "Common Themes in Christianity and Islam"),
                ("CSS755", "Patterns and Trends of Crime in Nigeria"),
                ("FRE101", "Basic French Grammar I"),
            ],

            (700, "Second Semester"): [
                ("PCR712", "Democracy and Good Governance"),
                ("PCR714", "Introduction to Conflict Resolution Processes II"),
                ("PCR716", "Research Methods in Peace Studies and Conflict Resolution"),
                ("PCR772", "Concept and Practice of Peace Building"),

                # Electives
                ("CRS704", "Religious Dialogue"),
                ("CSS742", "Policing and Law Enforcement in Nigeria"),
                ("FRE102", "Basic French Grammar and Composition II"),
            ],

            (700, "Third Semester"): [
                ("PCR718", "Project (Long Essay)"),
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
                "PGD Peace Studies and Conflict Resolution courses seeded successfully."
            )
        )