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
    help = "Seed B.A French and International Studies"

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
            name="French and International Studies"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A French and International Studies"
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
            ("GST101", "Use of English & Communication Skills I", level100, first_semester),
            ("GST105", "History and Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),
            ("CIT101", "Computers in Society", level100, first_semester),
            ("INR111", "Introduction to International Studies", level100, first_semester),
            ("INR121", "Structure of the International System", level100, first_semester),
            ("FRE121", "French Grammar I", level100, first_semester),
            ("FRE131", "Textual Analysis I", level100, first_semester),
            ("FRE141", "Introduction to Composition Writing in French", level100, first_semester),
            ("FRE111", "Language Laboratory Work / Oral French", level100, first_semester),

            # ==========================
            # 100 LEVEL SECOND SEMESTER
            # ==========================
            ("GST102", "Use of English & Communication Skills II", level100, second_semester),
            ("CIT102", "Application Software Skills", level100, second_semester),
            ("FRE122", "French Grammar II", level100, second_semester),
            ("FRE132", "Textual Analysis II", level100, second_semester),
            ("FRE142", "Composition Writing in French II", level100, second_semester),
            ("FRE112", "Oral French II", level100, second_semester),
            ("FRE162", "Introduction to Francophone African Culture and Civilization", level100, second_semester),
            ("INR122", "International Politics and Organizations", level100, second_semester),
            ("ECO121", "Principles of Economics I", level100, second_semester),

            # ==========================
            # 200 LEVEL FIRST SEMESTER
            # ==========================
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),
            ("FRE211", "French Phonetics and Phonology", level200, first_semester),
            ("FRE221", "Intermediate French Grammar", level200, first_semester),
            ("FRE231", "Introduction to French Literature", level200, first_semester),
            ("FRE241", "French Syntax", level200, first_semester),
            ("INR211", "Theories of International Relations", level200, first_semester),
            ("INR221", "International Law and Organizations", level200, first_semester),
            ("INR231", "Comparative Foreign Policy", level200, first_semester),

            # ==========================
            # 200 LEVEL SECOND SEMESTER
            # ==========================
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("FRE212", "French Morphology", level200, second_semester),
            ("FRE222", "Advanced French Grammar", level200, second_semester),
            ("FRE232", "Introduction to African Literature in French", level200, second_semester),
            ("FRE242", "French Language Skills I", level200, second_semester),
            ("INR212", "International Economic Relations", level200, second_semester),
            ("INR222", "Diplomacy and International Relations", level200, second_semester),
            ("INR232", "Nigerian Foreign Policy", level200, second_semester),

            # ==========================
            # 300 LEVEL FIRST SEMESTER
            # ==========================
            ("FRE311", "Advanced Studies in French Language Structure I", level300, first_semester),
            ("FRE321", "French Linguistics", level300, first_semester),
            ("FRE331", "Translation I", level300, first_semester),
            ("FRE341", "French Composition and Essay Writing", level300, first_semester),
            ("FRE361", "French Civilization", level300, first_semester),
            ("INR311", "International Politics", level300, first_semester),
            ("INR321", "Foreign Policy Analysis", level300, first_semester),
            ("INR331", "International Conflict and Security Studies", level300, first_semester),
            ("INR341", "International Organizations", level300, first_semester),

            # ==========================
            # 300 LEVEL SECOND SEMESTER
            # ==========================
            ("FRE312", "Advanced Studies in French Language Structure II", level300, second_semester),
            ("FRE322", "Applied French Linguistics", level300, second_semester),
            ("FRE332", "Translation II", level300, second_semester),
            ("FRE342", "French for Specific Purposes", level300, second_semester),
            ("FRE362", "Francophone African Civilization", level300, second_semester),
            ("INR312", "International Political Economy", level300, second_semester),
            ("INR322", "African International Relations", level300, second_semester),
            ("INR332", "Peace and Conflict Studies", level300, second_semester),
            ("INR342", "Strategic Studies", level300, second_semester),

            # ==========================
            # 400 LEVEL FIRST SEMESTER
            # ==========================
            ("FRE421", "Advanced Studies in French Language Structure III", level400, first_semester),
            ("FRE461", "French Civilization and Culture", level400, first_semester),
            ("FRE481", "19th Century French Literature", level400, first_semester),
            ("INR411", "Contemporary International Relations", level400, first_semester),
            ("INR421", "Seminar Presentation in International and Diplomatic Studies", level400, first_semester),
            ("INR431", "International Diplomacy", level400, first_semester),

            # ==========================
            # 400 LEVEL SECOND SEMESTER
            # ==========================
            ("FRE422", "Advanced Studies in French Language Structure IV", level400, second_semester),
            ("FRE423", "Linguistics Applied to the Teaching of French", level400, second_semester),
            ("FRE472", "Francophone Literature (Pre- and Post-Independence Poetry)", level400, second_semester),
            ("FRE482", "20th Century French Literature", level400, second_semester),
            ("INR412", "Foreign Policies of Great Powers", level400, second_semester),
            ("INR422", "International Institutions", level400, second_semester),
            ("INR432", "Afro-Asia Relations", level400, second_semester),
            ("FRE424/INR442", "Research Project", level400, second_semester),
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
                f"Successfully seeded {len(courses)} French and International Studies courses."
            )
        )