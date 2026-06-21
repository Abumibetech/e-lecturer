from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "NOUN Seeder (SAFE + NO DUPLICATES)"

    def handle(self, *args, **kwargs):

        # =========================
        # LEVELS
        # =========================
        levels = {}
        for i in range(100, 600, 100):
            levels[i], _ = Level.objects.get_or_create(name=i)

        # =========================
        # SEMESTERS
        # =========================
        sem1, _ = Semester.objects.get_or_create(name="First Semester")
        sem2, _ = Semester.objects.get_or_create(name="Second Semester")

        # =========================
        # DATA (SAMPLE STRUCTURE)
        # =========================
        data = {
            "FACULTY OF SOCIAL SCIENCES": {
                "Department of Criminology and Security Studies": {
                    "Criminology and Security Studies": [
                        (100, sem1, "CSS101", "Introduction to Criminology"),
                        (100, sem2, "CSS102", "Introduction to Sociology"),
                        (200, sem1, "CSS201", "Criminal Law"),
                        (200, sem2, "CSS202", "Penology"),
                        (300, sem1, "CSS301", "Criminal Investigation"),
                        (400, sem2, "CSS402", "Project Work"),
                    ]
                }
            }
        }

        created = 0

        for faculty_name, departments in data.items():

            faculty, _ = Faculty.objects.get_or_create(
                name=faculty_name,
                defaults={"slug": slugify(faculty_name)}
            )

            for dept_name, programmes in departments.items():

                department, _ = Department.objects.get_or_create(
                    name=dept_name,
                    faculty=faculty,
                    defaults={"slug": slugify(dept_name)}
                )

                for programme_name, courses in programmes.items():

                    programme, _ = Programme.objects.get_or_create(
                        name=programme_name,
                        department=department
                    )

                    for level, semester, code, title in courses:

                        Course.objects.get_or_create(
                            programme=programme,
                            level=levels[level],
                            semester=semester,
                            code=code,
                            defaults={"title": title}
                        )

                        created += 1

        self.stdout.write(self.style.SUCCESS(
            f"SEED COMPLETE → {created} courses processed"
        ))