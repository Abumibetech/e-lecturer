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
    help = "Seed B.Sc Agriculture"

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
            name="Agriculture"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc Agriculture"
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

            # 100 LEVEL FIRST SEMESTER
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

            # 100 LEVEL SECOND SEMESTER
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

            # 200 LEVEL FIRST SEMESTER
            ("AGR201", "General Agriculture", level200, first_semester),
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("FRM211", "Forestry and Wildlife Management", level200, first_semester),
            ("AGR205", "Introduction to Agro-Climatology", level200, first_semester),
            ("AGR203", "Principles of Crop Production", level200, first_semester),
            ("SLM201", "Principles of Soil Science", level200, first_semester),
            ("ARD203", "Introduction to Home Economics", level200, first_semester),
            ("ARD251", "Introduction to Agricultural Economics", level200, first_semester),
            ("ARD201", "Principles of Agricultural Extension", level200, first_semester),

            # 200 LEVEL SECOND SEMESTER
            ("CIT204", "Computer Appreciation and Application to Agriculture", level200, second_semester),
            ("AFS220", "Fisheries and Wildlife", level200, second_semester),
            ("FST202", "Principles of Food Science and Technology", level200, second_semester),
            ("AGR202", "Introductory Agricultural Engineering", level200, second_semester),
            ("ANP204", "Introductory Agricultural Biochemistry", level200, second_semester),
            ("ANP202", "Principles of Animal Production", level200, second_semester),
            ("ARD202", "Introduction to Rural Sociology", level200, second_semester),

            # 300 LEVEL FIRST SEMESTER
            ("ARD301", "Introduction to Agricultural Extension and Rural Development", level300, first_semester),
            ("ANP307", "Elementary Topics in Animal Breeding", level300, first_semester),
            ("ANP301", "Introduction to Non-Ruminant Animal Production", level300, first_semester),
            ("AGR305", "Analytical Techniques for Animal Production I", level300, first_semester),
            ("AEA302", "Agricultural Finance", level300, first_semester),
            ("AEA303", "Agricultural Production Economics", level300, first_semester),
            ("AEA304", "Agricultural Marketing and Price Analysis", level300, first_semester),
            ("AFM317", "Fish Health Management", level300, first_semester),
            ("AFM321", "Fisheries Management and Conservation", level300, first_semester),
            ("CRP303", "Permanent Crop Production", level300, first_semester),
            ("CRP309", "Arable Crops Production", level300, first_semester),
            ("CRP311", "Stored Produce Protection", level300, first_semester),
            ("CRP313", "Permanent Crop Production II", level300, first_semester),
            ("SLM303", "Introduction to Pedology and Soil Physics", level300, first_semester),
            ("AGR307", "Environmental Impact Assessment", level300, first_semester),

            # 300 LEVEL SECOND SEMESTER
            ("AGM314", "Introduction to Farm Mechanisation", level300, second_semester),
            ("ANP302", "Ruminant Animal Production", level300, second_semester),

            # 400 LEVEL FIRST SEMESTER
            ("ARD401", "Extension Practices", level400, first_semester),
            ("AEC401", "Farm Management Records and Accounts", level400, first_semester),
            ("SLM401", "Soil Fertility and Water Management", level400, first_semester),
            ("SLM403", "Farm Design, Survey and Land Use Planning", level400, first_semester),
            ("CRP401", "Crop Production Practice (Arable and Horticultural Crops)", level400, first_semester),
            ("CRP403", "Crop Protection Techniques", level400, first_semester),
            ("CRP405", "Agricultural Processing and Storage", level400, first_semester),
            ("ANP401", "Animal Husbandry Techniques I (Ruminants)", level400, first_semester),
            ("ANP403", "Animal Husbandry Techniques II (Non-Ruminants)", level400, first_semester),

            # 400 LEVEL SECOND SEMESTER
            ("AGR401", "Report Writing (Book Form)", level400, second_semester),
            ("AGM401", "Farm Mechanization Practices", level400, second_semester),
            ("AGM403", "Workshop Practice", level400, second_semester),
            ("AFS401", "Fisheries", level400, second_semester),
            ("AGR403", "Biotechnology in Agricultural Production", level400, second_semester),
            ("ANP407", "Animal Health Management", level400, second_semester),
            ("SLM405", "Agricultural Meteorology", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Agriculture courses."
            )
        )