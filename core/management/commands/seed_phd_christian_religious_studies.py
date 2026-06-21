from django.core.management.base import BaseCommand
from core.models import (
    Faculty,
    Department,
    Programme,
    Level,
    Semester,
    Course
)


class Command(BaseCommand):
    help = "Seed Ph.D Christian Religious Studies Courses"

    def handle(self, *args, **kwargs):

        faculty = Faculty.objects.filter(
            name__icontains="Arts"
        ).first()

        if not faculty:
            self.stdout.write(
                self.style.ERROR(
                    "Faculty of Arts not found."
                )
            )
            return

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Christian Religious Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Ph.D Christian Religious Studies"
        )

        courses = {

            (900, "First Semester"): [
                ("CRS901", "Advanced Research Methodology"),
                ("CRS903", "Advanced Seminar in Christian Theology"),
                ("CRS905", "Advanced Theoretical Perspectives in Theology"),
                ("CRS907", "Philosophy and Methods of Religious Research"),
            ],

            (900, "Second Semester"): [
                ("CRS912", "Doctoral Seminar I"),
                ("CRS914", "Contemporary Issues in Christian Theology"),
                ("CRS916", "Advanced Academic Writing and Publication"),
                ("CRS918", "Specialized Readings in Theology"),
                ("CRS920", "Thesis Proposal Development"),
            ],

            (900, "Third Semester"): [
                ("CRS991", "Thesis Research I"),
                ("CRS992", "Doctoral Seminar II"),
                ("CRS993", "Field Research"),
                ("CRS994", "Thesis Writing"),
            ],

            (900, "Fourth Semester"): [
                ("CRS999", "Doctoral Thesis"),
                ("CRS996", "Thesis Submission"),
                ("CRS997", "External Examination"),
                ("CRS998", "Viva Voce"),
            ],
        }

        total = 0

        for (level_num, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=level_num
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
                        "description": f"{title} ({code})"
                    }
                )

                total += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {total} Ph.D Christian Religious Studies courses."
            )
        )