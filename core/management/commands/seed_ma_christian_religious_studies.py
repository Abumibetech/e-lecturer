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
    help = "Seed M.A. Christian Religious Studies Courses"

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
            name="M.A. Christian Religious Studies"
        )

        courses = {

            (800, "First Semester"): [
                ("CRS801", "Advanced Research Method"),
                ("CRS847", "Christian Doctrines"),
                ("CRS841", "God and Revelation"),
                ("CRS843", "The Doctrine of the Holy Spirit"),
                ("CRS845", "Liberation and Feminist Theologies"),
                ("CRS899", "Dissertation"),
            ],

            (800, "Second Semester"): [
                ("CRS802", "Postgraduate Seminar"),
                ("CRS812", "Theology of the Pentateuch"),
                ("CRS836", "Ecclesiology"),
                ("CRS840", "Systematic Theology"),
                ("CRS842", "Christology"),
                ("CRS846", "African Christian Theologies"),
                ("CRS848", "Christian Apologetics"),
                ("CRS824", "New Testament Theology"),
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
                f"Successfully seeded {total} M.A. Christian Religious Studies courses."
            )
        )