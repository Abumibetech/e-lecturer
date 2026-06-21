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
    help = "Seed B.Sc Hospitality and Tourism Management"

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
            name="Hospitality and Tourism Management"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc Hospitality and Tourism Management"
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
            ("HCM131", "Introduction to Hospitality Management", level100, first_semester),
            ("HCM133", "Agriculture, Nutrition and Health", level100, first_semester),
            ("HCM135", "Introduction to Food and Beverage Services I", level100, first_semester),
            ("HCM141", "Understanding Tourism", level100, first_semester),
            ("HCM145", "Geography of Tourism", level100, first_semester),
            ("HCM147", "Tourism Policy and Planning", level100, first_semester),

            # ==========================
            # 100 LEVEL SECOND SEMESTER
            # ==========================
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("HCM134", "Food and Nutrition", level100, second_semester),
            ("HCM136", "Introduction to Food and Beverage Services II", level100, second_semester),
            ("HCM142", "Tourism as an Industry", level100, second_semester),
            ("HCM144", "Tourism Marketing", level100, second_semester),
            ("HCM146", "The Culture Heritage", level100, second_semester),

            # ==========================
            # 200 LEVEL FIRST SEMESTER
            # ==========================
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),
            ("HCM231", "Introduction to Food and Beverage Production I", level200, first_semester),
            ("HCM235", "Food, Beverage and Costs", level200, first_semester),
            ("HCM237", "Hospitality Sales and Marketing", level200, first_semester),
            ("HCM239", "Menu Planning and Catering Services", level200, first_semester),
            ("HCM243", "Tourist Sites: Products and Operations I", level200, first_semester),

            # ==========================
            # 200 LEVEL SECOND SEMESTER
            # ==========================
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("HCM210", "Industrial Training I", level200, second_semester),
            ("HCM232", "Menu Development and Planning", level200, second_semester),
            ("HCM234", "Facility Maintenance Management", level200, second_semester),
            ("HCM236", "Beverage Management", level200, second_semester),
            ("HCM238", "Introduction to Food and Beverage Production II", level200, second_semester),
            ("HCM241", "Understanding Tourists and Hosts", level200, second_semester),
            ("HCM244", "Tourist Sites: Products and Operations II", level200, second_semester),

            # ==========================
            # 300 LEVEL FIRST SEMESTER
            # ==========================
            ("HCM303", "Food Services and Professionalism", level300, first_semester),
            ("HCM305", "Tourism Sales and Marketing", level300, first_semester),
            ("HCM313", "Restaurant Entrepreneurship", level300, first_semester),
            ("HCM333", "Food and Beverage Services III", level300, first_semester),
            ("HCM339", "Food and Beverage Production III", level300, first_semester),
            ("HCM343", "Procurement and Supply Management", level300, first_semester),
            ("HCM345", "Wine and Food Pairing Principles", level300, first_semester),
            ("HCM347", "Commercial Recreation Management", level300, first_semester),
            ("HCM349", "Introduction to Airline Management", level300, first_semester),

            # ==========================
            # 300 LEVEL SECOND SEMESTER
            # ==========================
            ("HCM304", "Food and Beverage Production IV", level300, second_semester),
            ("HCM310", "Industrial Training II", level300, second_semester),
            ("HCM340", "Hospitality Laws and Travels", level300, second_semester),
            ("HCM342", "Current Issues in Food Safety and Sanitation", level300, second_semester),
            ("HCM348", "Hospitality and Tourism Management", level300, second_semester),

            # ==========================
            # 400 LEVEL FIRST SEMESTER
            # ==========================
            ("HCM431", "Advanced Food and Beverage Production", level400, first_semester),
            ("HCM433", "Management and Organizational Behaviour", level400, first_semester),
            ("HCM435", "Security and Loss Prevention Management", level400, first_semester),
            ("HCM437", "Advanced Food and Beverage Services", level400, first_semester),
            ("HCM439", "Hotel Planning and Interior Design", level400, first_semester),
            ("TSM403", "Cultural Tourism", level400, first_semester),
            ("TSM441", "Strategic Management in Hospitality and Tourism", level400, first_semester),

            # ==========================
            # 400 LEVEL SECOND SEMESTER
            # ==========================
            ("HCM412", "Seminar in Hotel and Catering Management", level400, second_semester),
            ("HCM432", "Hospitality Information Systems", level400, second_semester),
            ("HCM434", "Lodging Facilities Management", level400, second_semester),
            ("HCM436", "Internal Control in Hospitality Administration", level400, second_semester),
            ("HCM438", "Hospitality Supervision and Quality Management", level400, second_semester),
            ("HCM442", "Tourism Entrepreneurship", level400, second_semester),
            ("HCM444", "Global Tourism Issues", level400, second_semester),
            ("HCM450", "Research Project", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Hospitality and Tourism Management courses."
            )
        )