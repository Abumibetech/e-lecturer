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
    help = "Seed Agricultural Extension and Management"

    def handle(self, *args, **kwargs):

        # ==========================================
        # FACULTY
        # ==========================================
        faculty, _ = Faculty.objects.get_or_create(
            name="Agricultural Sciences"
        )

        # ==========================================
        # DEPARTMENT
        # ==========================================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Agricultural Extension and Management"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Agricultural Extension and Management"
        )

        # ==========================================
        # LEVEL
        # ==========================================
        level700, _ = Level.objects.get_or_create(name=700)

        # ==========================================
        # SEMESTERS
        # ==========================================
        first_semester, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        second_semester, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        # ==========================================
        # COURSES
        # ==========================================
        courses = [

            # 700L FIRST SEMESTER
            ("CIT101", "Computers in Society", level700, first_semester),
            ("GST707", "The Good Study Guide", level700, first_semester),
            ("AEM701", "Agricultural Extension Education", level700, first_semester),
            ("AEM715", "Management of Agricultural Extension Personnel", level700, first_semester),
            ("AEM719", "Extension Methods and Communication", level700, first_semester),
            ("AEM741", "Rural Sociology", level700, first_semester),
            ("AEM753", "Farm Management", level700, first_semester),
            ("AEM757", "Agricultural Extension Administration and Supervision", level700, first_semester),

            # ELECTIVES - FIRST SEMESTER
            ("AEM713", "Tree Crops Production", level700, first_semester),
            ("AEM751", "Micro Economics", level700, first_semester),
            ("AEM773", "Management of Non-Ruminant Animals", level700, first_semester),

            # 700L SECOND SEMESTER
            ("AEM712", "Agricultural Extension Administration, Programme Planning and Evaluation", level700, second_semester),
            ("AEM732", "Women and Youth in Rural Development Programme", level700, second_semester),
            ("AEM736", "Extension Organisation and Management", level700, second_semester),
            ("AEM738", "Rural Development and Leadership", level700, second_semester),
            ("AEM772", "Statistics and Research Methods in Extension", level700, second_semester),
            ("AEM724", "Macro Economics", level700, second_semester),
            ("AEM790", "Project", level700, second_semester),

            # ELECTIVES - SECOND SEMESTER
            ("AEM716", "Agricultural Marketing and Cooperatives", level700, second_semester),
            ("AEM722", "Ruminant Animals", level700, second_semester),
        ]

        for code, title, level, semester in courses:
            Course.objects.get_or_create(
                programme=programme,
                code=code,
                defaults={
                    "title": title,
                    "level": level,
                    "semester": semester,
                    "description": title,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(courses)} Agricultural Extension and Management courses."
            )
        )