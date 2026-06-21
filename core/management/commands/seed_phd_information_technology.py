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
    help = "Seed PhD Information Technology courses"

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
            name="PhD Information Technology"
        )

        courses = {

            (900, "First Semester"): [
                ("CIT901", "Survey of Recent Development in Network Technologies and Securities (Seminar I)"),
                ("CIT903", "Advanced Artificial Intelligence"),

                # Electives
                ("CIT905", "Advanced Database Management Systems"),
                ("CIT907", "Advanced Operational Research"),
            ],

            (900, "Second Semester"): [
                ("CIT902", "Seminar on ICT Research Methodology and Statistics"),
                ("CIT912", "Seminar on Advanced System Analysis and Design"),

                # Research Electives (Departmental Approval)
                ("CIT913", "Special Topics in Information Technology (Approved Research Topic)"),
                ("CIT914", "Directed Research in Information Technology"),
                ("CIT915", "Advanced Seminar Topics in Information Technology"),
            ],

            (900, "First Year - First Semester"): [
                ("PHD901", "Doctoral Seminar I"),
                ("PHD991", "Dissertation Research I"),
            ],

            (900, "First Year - Second Semester"): [
                ("PHD902", "Doctoral Seminar II"),
                ("PHD992", "Dissertation Research II"),
            ],

            (900, "Second Year - First Semester"): [
                ("PHD993", "Dissertation Research III"),
            ],

            (900, "Second Year - Second Semester"): [
                ("PHD999", "PhD Thesis / Dissertation"),
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
                "PhD Information Technology courses seeded successfully."
            )
        )