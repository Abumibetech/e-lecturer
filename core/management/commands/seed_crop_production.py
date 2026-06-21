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
    help = "Seed B.Sc Crop Production"

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
            name="Crop Production"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc Crop Production"
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
            ("CHM132", "Organic Chemistry for Agriculture II", level100, second_semester),
            ("BIO102", "General Biology II", level100, second_semester),
            ("CHM192", "Practical Chemistry II", level100, second_semester),
            ("PHY192", "Practical Physics II", level100, second_semester),
            ("BIO192", "Practical Biology II", level100, second_semester),
            ("AGR102", "Mathematics for Agriculture II", level100, second_semester),
            ("CHM102", "Physical Chemistry", level100, second_semester),
            ("GST104", "Introduction to Social Sciences", level100, second_semester),

            # 200 LEVEL FIRST SEMESTER
            ("AGR201", "General Agriculture", level200, first_semester),
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("FRM211", "Forestry and Wildlife Management", level200, first_semester),
            ("AGR205", "Introduction to Agro-Climatology", level200, first_semester),
            ("AGR203", "Principles of Crop Production", level200, first_semester),
            ("SLM201", "Principles of Soil Science", level200, first_semester),
            ("ARD203", "Introduction to Home Economics", level200, first_semester),
            ("ARD201", "Principles of Agricultural Extension", level200, first_semester),
            ("AEA251", "Introduction to Agricultural Economics", level200, first_semester),

            # 200 LEVEL SECOND SEMESTER
            ("AGR202", "Introductory Agricultural Engineering", level200, second_semester),
            ("AGR204", "Crop Physiology", level200, second_semester),
            ("CRP202", "Introduction to Crop Science", level200, second_semester),
            ("CRP204", "Principles of Plant Genetics", level200, second_semester),
            ("CRP206", "Introduction to Plant Breeding", level200, second_semester),
            ("SLM202", "Soil Chemistry", level200, second_semester),
            ("CIT204", "Computer Applications in Agriculture", level200, second_semester),
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),

            # 300 LEVEL FIRST SEMESTER
            ("CRP301", "Crop Physiology", level300, first_semester),
            ("CRP303", "Permanent Crop Production", level300, first_semester),
            ("CRP305", "Principles of Crop Protection", level300, first_semester),
            ("CRP307", "Seed Science and Technology", level300, first_semester),
            ("CRP309", "Arable Crop Production", level300, first_semester),
            ("CRP311", "Stored Produce Protection", level300, first_semester),
            ("SLM303", "Introduction to Pedology and Soil Physics", level300, first_semester),
            ("AGR307", "Environmental Impact Assessment", level300, first_semester),

            # 300 LEVEL SECOND SEMESTER
            ("CRP302", "Plant Breeding Techniques", level300, second_semester),
            ("CRP304", "Principles of Horticultural Crop Production", level300, second_semester),
            ("CRP306", "Principles of Irrigation and Drainage", level300, second_semester),
            ("CRP308", "Weed Science and Management", level300, second_semester),
            ("CRP310", "Crop Improvement", level300, second_semester),
            ("CRP312", "Crop Production Systems", level300, second_semester),
            ("AGR302", "Agricultural Statistics", level300, second_semester),
            ("ENT300", "Entrepreneurship Studies", level300, second_semester),

            # 400 LEVEL FIRST SEMESTER
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
            ("CRP499", "Research Project", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Crop Production courses."
            )
        )