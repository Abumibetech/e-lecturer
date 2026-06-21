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
    help = "Seed Agricultural Extension and Rural Sociology"

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
            name="Agricultural Extension and Rural Sociology"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Agricultural Extension and Rural Sociology"
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
            ("GST105", "History and Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),
            ("BIO101", "General Biology I", level100, first_semester),
            ("BIO191", "General Biology Practical I", level100, first_semester),
            ("CHM101", "Introductory Inorganic Chemistry I", level100, first_semester),
            ("CHM191", "Introductory Practical Chemistry I", level100, first_semester),
            ("CIT101", "Computers in Society", level100, first_semester),
            ("MTH133", "Trigonometry", level100, first_semester),
            ("PHY111", "Elementary Mechanics", level100, first_semester),
            ("PHY191", "Introductory Practical Physics I", level100, first_semester),

            # 100L SECOND SEMESTER
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("CHM132", "Organic Chemistry for Agriculture II", level100, second_semester),
            ("BIO102", "General Biology II", level100, second_semester),
            ("CHM192", "Introductory Practical Chemistry II", level100, second_semester),
            ("PHY192", "Practical Physics II", level100, second_semester),
            ("BIO192", "General Biology Practical II", level100, second_semester),
            ("AGR102", "Mathematics for Agriculture II", level100, second_semester),
            ("CHM102", "Physical Chemistry", level100, second_semester),
            ("GST104", "Introduction to Social Sciences", level100, second_semester),

            # 200L FIRST SEMESTER
            ("ARD201", "Principles of Agricultural Extension", level200, first_semester),
            ("AEA251", "Introduction to Agricultural Economics", level200, first_semester),
            ("AGR201", "General Agriculture", level200, first_semester),
            ("ARD203", "Introduction to Home Economics", level200, first_semester),
            ("SLM201", "Principles of Soil Science", level200, first_semester),
            ("AGR203", "Principles of Crop Production", level200, first_semester),
            ("AGR205", "Introduction to Agro-Climatology", level200, first_semester),
            ("FRM211", "Forestry and Wildlife Management", level200, first_semester),
            ("ANP201", "Introduction to Biotechnology", level200, first_semester),
            ("AGR207", "Anatomy and Physiology of Farm Animals", level200, first_semester),
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),

            # 200L SECOND SEMESTER
            ("ARD202", "Rural Sociology", level200, second_semester),
            ("ARD204", "Principles of Community Development", level200, second_semester),
            ("AEA202", "Principles of Agricultural Economics II", level200, second_semester),
            ("AGR204", "Crop Physiology", level200, second_semester),
            ("AGR206", "Agricultural Production Systems", level200, second_semester),
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("ENT202", "Entrepreneurship Studies", level200, second_semester),
            ("STA202", "Statistics for Agriculture", level200, second_semester),

            # 300L FIRST SEMESTER
            ("ARD301", "Agricultural Extension Methods", level300, first_semester),
            ("ARD303", "Agricultural Communication", level300, first_semester),
            ("ARD305", "Extension Teaching Methods", level300, first_semester),
            ("ARD307", "Rural Leadership Development", level300, first_semester),
            ("ARD309", "Agricultural Information Systems", level300, first_semester),
            ("AEA301", "Agricultural Development and Policy", level300, first_semester),
            ("AEA303", "Farm Management Analysis", level300, first_semester),
            ("ENT301", "Entrepreneurship in Agriculture", level300, first_semester),

            # 300L SECOND SEMESTER
            ("CRP312", "Farm Power and Agricultural Mechanisation", level300, second_semester),
            ("AEA302", "Agricultural Finance and Marketing", level300, second_semester),
            ("AEA304", "Agricultural Marketing and Price Analysis", level300, second_semester),
            ("ARD304", "Communication Audio-Visual Techniques", level300, second_semester),
            ("AEA310", "Farm Business Organisation", level300, second_semester),
            ("AEA306", "Farm Records and Accounting", level300, second_semester),
            ("AEA308", "Principles of Farm Management", level300, second_semester),
            ("ANP302", "Introduction to Ruminant Animal Production", level300, second_semester),
            ("ENT310", "Cultural Change and Entrepreneurship", level300, second_semester),

            # 400L FIRST SEMESTER
            ("AGR400", "Farm Practical Year / SIWES", level400, first_semester),
            ("AGR401", "Agricultural Extension Field Practice", level400, first_semester),
            ("AGR402", "Rural Development Field Experience", level400, first_semester),
            ("AGR403", "Community-Based Agricultural Project", level400, first_semester),
            ("AGR404", "Farm Enterprise Management Practice", level400, first_semester),

            # 400L SECOND SEMESTER
            ("AGR405", "Continuation of Farm Practical Year / SIWES", level400, second_semester),
            ("AGR406", "Extension Programme Evaluation", level400, second_semester),
            ("AGR407", "Agricultural Innovation Management", level400, second_semester),
            ("AGR408", "Rural Development Assessment", level400, second_semester),
            ("AGR409", "Seminar and Report Writing", level400, second_semester),
            ("AGR410", "Project Preparation", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Agricultural Extension and Rural Sociology courses."
            )
        )