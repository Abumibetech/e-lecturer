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
    help = "Seed Agricultural Extension and Rural Development"

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
            name="Agricultural Extension and Rural Development"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Agricultural Extension and Rural Development"
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

            # 100L FIRST SEMESTER
            ("GST101", "Use of English and Communication Skills I", level100, first_semester),
            ("CIT101", "Computers in Society", level100, first_semester),
            ("GST121", "Use of Library", level100, first_semester),
            ("GST105", "History and Philosophy of Science", level100, first_semester),
            ("BIO101", "General Biology I", level100, first_semester),
            ("BIO191", "Practical Biology I", level100, first_semester),
            ("CHM101", "Introduction to Inorganic Chemistry I", level100, first_semester),
            ("CHM191", "Practical Chemistry I", level100, first_semester),
            ("AGR101", "Mathematics for Agriculture I", level100, first_semester),
            ("PHY121", "General Physics I", level100, first_semester),
            ("PHY191", "Practical Physics I", level100, first_semester),
            ("CHM131", "Organic Chemistry for Agriculture I", level100, first_semester),

            # 100L SECOND SEMESTER
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("CIT102", "Application Software Skills", level100, second_semester),
            ("BIO102", "General Biology II", level100, second_semester),
            ("BIO192", "Practical Biology II", level100, second_semester),
            ("CHM102", "Introduction to Inorganic Chemistry II", level100, second_semester),
            ("CHM192", "Practical Chemistry II", level100, second_semester),
            ("AGR102", "Mathematics for Agriculture II", level100, second_semester),
            ("PHY122", "General Physics II", level100, second_semester),
            ("PHY192", "Practical Physics II", level100, second_semester),
            ("CHM132", "Organic Chemistry for Agriculture II", level100, second_semester),
            ("GST107", "The Good Study Guide", level100, second_semester),

            # 200L FIRST SEMESTER
            ("ARD201", "Introduction to Agricultural Extension and Rural Development", level200, first_semester),
            ("ARD203", "Introduction to Home Economics", level200, first_semester),
            ("AGR203", "Principles of Crop Production", level200, first_semester),
            ("AGR205", "Introduction to Agro-Climatology", level200, first_semester),
            ("FRM211", "Forestry and Wildlife Management", level200, first_semester),
            ("SLM201", "Principles of Soil Science", level200, first_semester),
            ("ANP201", "Principles of Animal Production", level200, first_semester),
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),

            # 200L SECOND SEMESTER
            ("ARD202", "Rural Sociology", level200, second_semester),
            ("ARD204", "Principles of Community Development", level200, second_semester),
            ("AGR204", "Crop Physiology", level200, second_semester),
            ("AGR206", "Agricultural Economics", level200, second_semester),
            ("ANP202", "Animal Production Systems", level200, second_semester),
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("ENT202", "Entrepreneurship Studies", level200, second_semester),
            ("STA202", "Statistics for Agriculture", level200, second_semester),

            # 300L FIRST SEMESTER
            ("ARD301", "Principles of Agricultural Extension", level300, first_semester),
            ("ARD303", "Communication in Agricultural Extension", level300, first_semester),
            ("ARD305", "Extension Teaching Methods", level300, first_semester),
            ("ARD307", "Rural Leadership Development", level300, first_semester),
            ("ARD309", "Agricultural Information Systems", level300, first_semester),
            ("AGR301", "Farm Management", level300, first_semester),
            ("AGR303", "Agricultural Marketing", level300, first_semester),
            ("ENT301", "Entrepreneurship in Agriculture", level300, first_semester),

            # 300L SECOND SEMESTER
            ("ARD302", "Agricultural Extension Programme Planning", level300, second_semester),
            ("ARD304", "Rural Development Strategies", level300, second_semester),
            ("ARD306", "Agricultural Journalism", level300, second_semester),
            ("ARD308", "Extension Administration", level300, second_semester),
            ("ARD310", "Project Planning and Evaluation", level300, second_semester),
            ("AGR302", "Farm Records and Accounts", level300, second_semester),
            ("AGR304", "Agricultural Finance", level300, second_semester),
            ("APT300", "Agricultural Practical Training", level300, second_semester),

            # 400L FIRST SEMESTER
            ("ARD401", "Agricultural Extension Administration", level400, first_semester),
            ("ARD403", "Rural Social Change", level400, first_semester),
            ("ARD405", "Agricultural Innovation and Technology Transfer", level400, first_semester),
            ("ARD407", "Community Development Practice", level400, first_semester),
            ("ARD409", "Agricultural Communication and Media", level400, first_semester),
            ("AGR401", "Agribusiness Management", level400, first_semester),
            ("AGR403", "Farm Management and Finance", level400, first_semester),
            ("ARD491", "Seminar", level400, first_semester),

            # 400L SECOND SEMESTER
            ("ARD402", "Diffusion and Adoption of Innovations", level400, second_semester),
            ("ARD404", "Agricultural Extension Programme Evaluation", level400, second_semester),
            ("ARD406", "Rural Development Policy", level400, second_semester),
            ("ARD408", "Community Organization and Leadership", level400, second_semester),
            ("ARD410", "Extension Project Management", level400, second_semester),
            ("ARD499", "Research Project", level400, second_semester),
            ("AGR404", "Agricultural Enterprise Development", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Agricultural Extension and Rural Development courses."
            )
        )