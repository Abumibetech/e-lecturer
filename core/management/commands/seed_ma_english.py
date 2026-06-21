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
    help = "Seed M.A English"

    def handle(self, *args, **kwargs):

        # ==========================================
        # FACULTY
        # ==========================================
        faculty, _ = Faculty.objects.get_or_create(
            name="Arts"
        )

        # ==========================================
        # DEPARTMENT
        # ==========================================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="English Studies"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.A English"
        )

        # ==========================================
        # LEVEL
        # ==========================================
        level800, _ = Level.objects.get_or_create(name=800)

        # ==========================================
        # SEMESTERS
        # ==========================================
        first_semester, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        second_semester, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        third_semester, _ = Semester.objects.get_or_create(
            name="Third Semester"
        )

        # ==========================================
        # COURSES
        # ==========================================
        courses = [

            # ==================================
            # 800L FIRST SEMESTER
            # ==================================
            ("ENG801", "Advanced English Phonetics and Phonology", level800, first_semester),
            ("ENG802", "Advanced English Syntax and Morphology", level800, first_semester),
            ("ENG803", "Advanced English Semantics and Lexicology", level800, first_semester),
            ("ENG804", "Advanced Discourse Analysis", level800, first_semester),
            ("ENG805", "Advanced Stylistics", level800, first_semester),
            ("ENG811", "Advanced Research Methods in English", level800, first_semester),
            ("ENG812", "Contrastive Linguistics", level800, first_semester),

            # ==================================
            # 800L SECOND SEMESTER
            # LANGUAGE OPTION
            # ==================================
            ("ENG833", "Pragmatics", level800, second_semester),
            ("ENG836", "Semiotics", level800, second_semester),
            ("ENG841", "Advanced Sociolinguistics", level800, second_semester),
            ("ENG846", "Advanced Varieties of English", level800, second_semester),
            ("ENG851", "Bilingualism and Multilingualism", level800, second_semester),
            ("ENG855", "Translation Studies", level800, second_semester),
            ("ENG858", "English as a Second Language", level800, second_semester),
            ("ENG891", "Psycholinguistics", level800, second_semester),

            # ==================================
            # 800L SECOND SEMESTER
            # LITERATURE OPTION
            # ==================================
            ("ENG814", "Studies in African Oral Literature", level800, second_semester),
            ("ENG815", "Advanced Literary Theory and Criticism", level800, second_semester),
            ("ENG817", "African-American and Caribbean Literature", level800, second_semester),
            ("ENG819", "Modern European Literature", level800, second_semester),
            ("ENG823", "Popular Literature and Mass Media", level800, second_semester),
            ("ENG825", "Advanced Creative Writing", level800, second_semester),
            ("ENG871", "Studies in African Poetry", level800, second_semester),
            ("ENG861", "Studies in African Drama", level800, second_semester),
            ("ENG881", "Studies in African Fiction", level800, second_semester),

            # ==================================
            # 800L THIRD SEMESTER
            # ==================================
            ("ENG810", "M.A. Dissertation", level800, third_semester),
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
                f"Successfully seeded {len(courses)} M.A English courses."
            )
        )