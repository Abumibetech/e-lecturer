from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Business Administration Programme"

    def handle(self, *args, **kwargs):

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Management Sciences",
            defaults={"slug": "management-sciences"}
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Business Administration",
            defaults={"slug": "business-administration"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Business Administration"
        )

        # =========================
        # LEVELS
        # =========================
        level100, _ = Level.objects.get_or_create(name=100)
        level200, _ = Level.objects.get_or_create(name=200)
        level300, _ = Level.objects.get_or_create(name=300)
        level400, _ = Level.objects.get_or_create(name=400)

        # =========================
        # SEMESTERS
        # =========================
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
            (100, first_semester, "GST101", "Use of English and Communication Skills I"),
            (100, first_semester, "GST105", "History and Philosophy of Science"),
            (100, first_semester, "GST107", "The Good Study Guide"),
            (100, first_semester, "CIT101", "Computers in Society"),
            (100, first_semester, "MTH101", "Elementary Mathematics I"),
            (100, first_semester, "ECO101", "Introduction to Economics I"),
            (100, first_semester, "ACC101", "Principles of Accounting I"),
            (100, first_semester, "BUS101", "Introduction to Business"),
            (100, first_semester, "MKT101", "Principles of Marketing"),
            (100, first_semester, "BUS103", "Business Communication"),

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
            (100, second_semester, "GST102", "Use of English and Communication Skills II"),
            (100, second_semester, "ECO102", "Introduction to Economics II"),
            (100, second_semester, "ACC102", "Principles of Accounting II"),
            (100, second_semester, "BUS102", "Business Law"),
            (100, second_semester, "MTH102", "Elementary Mathematics II"),
            (100, second_semester, "BUS104", "Principles of Management"),
            (100, second_semester, "STA102", "Introduction to Statistics"),
            (100, second_semester, "BUS106", "Business Environment"),

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "ACC201", "Financial Accounting I"),
            (200, first_semester, "ECO201", "Microeconomics I"),
            (200, first_semester, "BUS201", "Organizational Behaviour"),
            (200, first_semester, "MKT201", "Marketing Management I"),
            (200, first_semester, "BUS203", "Business Ethics"),
            (200, first_semester, "BUS205", "Quantitative Techniques I"),

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, second_semester, "GST202", "Peace Studies and Conflict Resolution"),
            (200, second_semester, "ACC202", "Financial Accounting II"),
            (200, second_semester, "ECO202", "Microeconomics II"),
            (200, second_semester, "BUS202", "Human Resource Management I"),
            (200, second_semester, "MKT202", "Marketing Management II"),
            (200, second_semester, "BUS204", "Operations Management"),
            (200, second_semester, "BUS206", "Business Research Methods"),
            (200, second_semester, "BUS208", "Quantitative Techniques II"),

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "BUS301", "Production and Operations Management"),
            (300, first_semester, "BUS303", "Human Resource Management II"),
            (300, first_semester, "BUS305", "Management Information Systems"),
            (300, first_semester, "ACC301", "Management Accounting"),
            (300, first_semester, "MKT301", "Consumer Behaviour"),
            (300, first_semester, "BUS307", "Business Law II"),
            (300, first_semester, "BUS309", "Public Administration Basics"),

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, second_semester, "BUS302", "Strategic Management I"),
            (300, second_semester, "BUS304", "Organizational Theory"),
            (300, second_semester, "BUS306", "Entrepreneurship Development"),
            (300, second_semester, "BUS308", "Business Research Methods II"),
            (300, second_semester, "BUS310", "International Business Management"),
            (300, second_semester, "BUS312", "Industrial Relations"),
            (300, second_semester, "EDU300", "SIWES"),

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, first_semester, "BUS401", "Strategic Management II"),
            (400, first_semester, "BUS403", "Business Policy"),
            (400, first_semester, "BUS405", "Leadership and Corporate Governance"),
            (400, first_semester, "BUS407", "Small Business Management"),
            (400, first_semester, "BUS409", "Project Management"),
            (400, first_semester, "BUS411", "Business Seminar"),

            # =========================
            # ELECTIVES (400L FIRST)
            # =========================
            (400, first_semester, "BUS413", "Public Sector Management"),
            (400, first_semester, "BUS415", "International Business Strategy"),

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, second_semester, "BUS402", "Entrepreneurship and Innovation"),
            (400, second_semester, "BUS404", "Business Ethics and Corporate Social Responsibility"),
            (400, second_semester, "BUS406", "Business Forecasting and Decision Making"),
            (400, second_semester, "BUS408", "Project (Final Year Research Project)"),
            (400, second_semester, "BUS410", "Advanced Management Theory"),

            # =========================
            # ELECTIVES (400L SECOND)
            # =========================
            (400, second_semester, "BUS412", "Cooperative Management"),
            (400, second_semester, "BUS414", "Logistics and Supply Chain Management"),
        ]

        levels = {
            100: level100,
            200: level200,
            300: level300,
            400: level400,
        }

        created = 0

        for level_num, semester, code, title in courses:
            _, was_created = Course.objects.get_or_create(
                programme=programme,
                level=levels[level_num],
                semester=semester,
                code=code,
                defaults={
                    "title": title,
                    "description": title,
                }
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {created} Business Administration courses"
            )
        )