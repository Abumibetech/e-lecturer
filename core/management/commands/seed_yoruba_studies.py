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
    help = "Seed B.A Yoruba Studies"

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
            name="Yoruba Studies"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A Yoruba Studies"
        )

        # ==========================================
        # LEVELS
        # ==========================================
        level100, _ = Level.objects.get_or_create(name=100)
        level200, _ = Level.objects.get_or_create(name=200)
        level300, _ = Level.objects.get_or_create(name=300)
        level400, _ = Level.objects.get_or_create(name=400)

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

            # ==========================
            # 100 LEVEL FIRST SEMESTER
            # ==========================
            ("GST101", "Use of English and Communication Skills I", level100, first_semester),
            ("GST105", "History and Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),
            ("CIT101", "Computers in Society", level100, first_semester),
            ("YOR111", "Introduction to Yoruba Language I", level100, first_semester),
            ("YOR113", "Introduction to Yoruba Phonetics and Phonology", level100, first_semester),
            ("YOR115", "Yoruba Oral Literature I", level100, first_semester),
            ("YOR117", "Introduction to Yoruba Culture and Civilization", level100, first_semester),
            ("YOR119", "Reading and Writing Skills in Yoruba", level100, first_semester),

            # ==========================
            # 100 LEVEL SECOND SEMESTER
            # ==========================
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("CIT102", "Application Software Skills", level100, second_semester),
            ("YOR112", "Introduction to Yoruba Language II", level100, second_semester),
            ("YOR114", "Elementary Yoruba Grammar", level100, second_semester),
            ("YOR116", "Yoruba Oral Literature II", level100, second_semester),
            ("YOR118", "Yoruba Folklore and Traditional Institutions", level100, second_semester),
            ("YOR120", "Yoruba Composition I", level100, second_semester),

            # ==========================
            # 200 LEVEL FIRST SEMESTER
            # ==========================
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),
            ("YOR211", "Yoruba Morphology", level200, first_semester),
            ("YOR213", "Intermediate Yoruba Syntax", level200, first_semester),
            ("YOR215", "Yoruba Composition II", level200, first_semester),
            ("YOR217", "Yoruba Drama and Poetry", level200, first_semester),
            ("YOR219", "Yoruba Dialect Studies", level200, first_semester),
            ("YOR221", "Traditional Yoruba Religion and Belief Systems", level200, first_semester),

            # ==========================
            # 200 LEVEL SECOND SEMESTER
            # ==========================
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("YOR212", "Yoruba Phonology", level200, second_semester),
            ("YOR214", "Yoruba Written Literature I", level200, second_semester),
            ("YOR216", "Yoruba Written Literature II", level200, second_semester),
            ("YOR218", "Yoruba Culture and Civilization", level200, second_semester),
            ("YOR220", "Yoruba Lexicography", level200, second_semester),
            ("YOR222", "Introduction to Yoruba Literary Criticism", level200, second_semester),

            # ==========================
            # 300 LEVEL FIRST SEMESTER
            # ==========================
            ("YOR311", "Advanced Yoruba Syntax", level300, first_semester),
            ("YOR313", "Yoruba Semantics", level300, first_semester),
            ("YOR315", "Yoruba Stylistics", level300, first_semester),
            ("YOR317", "Translation Theory and Practice I", level300, first_semester),
            ("YOR319", "Modern Yoruba Literature", level300, first_semester),
            ("YOR321", "Research Methods in Yoruba Studies", level300, first_semester),
            ("GST302", "Entrepreneurship and Innovation", level300, first_semester),

            # ==========================
            # 300 LEVEL SECOND SEMESTER
            # ==========================
            ("YOR312", "Yoruba Pragmatics and Discourse Analysis", level300, second_semester),
            ("YOR314", "Translation Theory and Practice II", level300, second_semester),
            ("YOR316", "Contemporary Yoruba Literature", level300, second_semester),
            ("YOR318", "Yoruba Language in the Media", level300, second_semester),
            ("YOR320", "Comparative African Languages", level300, second_semester),
            ("YOR322", "Contemporary Issues in Yoruba Studies", level300, second_semester),

            # ==========================
            # 400 LEVEL FIRST SEMESTER
            # ==========================
            ("YOR411", "Advanced Yoruba Communication", level400, first_semester),
            ("YOR413", "Yoruba Literary Criticism", level400, first_semester),
            ("YOR415", "Yoruba Philosophy and Thought", level400, first_semester),
            ("YOR417", "Yoruba Oral Traditions and Performance", level400, first_semester),
            ("YOR419", "Yoruba in Contemporary Society", level400, first_semester),
            ("YOR421", "Seminar in Yoruba Studies", level400, first_semester),

            # ==========================
            # 400 LEVEL SECOND SEMESTER
            # ==========================
            ("YOR412", "Advanced Yoruba Stylistics", level400, second_semester),
            ("YOR414", "Yoruba Language Planning and Development", level400, second_semester),
            ("YOR416", "Yoruba and African Cultural Studies", level400, second_semester),
            ("YOR418", "Special Topics in Yoruba Studies", level400, second_semester),
            ("YOR420", "Project / Long Essay", level400, second_semester),
            ("YOR422", "Field Research in Yoruba Language and Culture", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Yoruba Studies courses."
            )
        )