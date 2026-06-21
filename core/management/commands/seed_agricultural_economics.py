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
    help = "Seed Agricultural Economics and Agribusiness"

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
            name="Agricultural Economics and Extension"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Agricultural Economics and Agribusiness"
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
            ("CIT102", "Software Application Skills", level100, second_semester),
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
            ("AEA201", "Principles of Agricultural Economics", level200, first_semester),
            ("AEA203", "Introduction to Farm Management", level200, first_semester),
            ("AEA205", "Agricultural Marketing", level200, first_semester),
            ("ARD201", "Introduction to Agricultural Extension", level200, first_semester),
            ("CSC201", "Principles of Crop Production", level200, first_semester),
            ("ANP201", "Principles of Animal Production", level200, first_semester),
            ("STA201", "Statistics for Agriculture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),

            # 200L SECOND SEMESTER
            ("AEA202", "Microeconomics for Agriculture", level200, second_semester),
            ("AEA204", "Agricultural Production Economics", level200, second_semester),
            ("AEA206", "Cooperative Organization and Management", level200, second_semester),
            ("ARD202", "Rural Sociology", level200, second_semester),
            ("CSC202", "Soil Science", level200, second_semester),
            ("ANP202", "Livestock Production Systems", level200, second_semester),
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),
            ("ENT202", "Entrepreneurship Studies", level200, second_semester),

            # 300L FIRST SEMESTER
            ("AEA301", "Agricultural Development and Policy", level300, first_semester),
            ("AEA303", "Farm Management Analysis", level300, first_semester),
            ("AEA305", "Introduction to Agribusiness Management", level300, first_semester),
            ("AEA307", "Agricultural Project Planning", level300, first_semester),
            ("ARD301", "Rural Development", level300, first_semester),
            ("AEA309", "Agricultural Statistics", level300, first_semester),
            ("ENT301", "Entrepreneurship in Agriculture", level300, first_semester),
            ("CSC301", "Crop Protection", level300, first_semester),

            # 300L SECOND SEMESTER
            ("AEA302", "Agricultural Finance and Marketing", level300, second_semester),
            ("AEA304", "Agricultural Marketing and Price Analysis", level300, second_semester),
            ("ARD304", "Communication and Audio-Visual Techniques", level300, second_semester),
            ("AEA310", "Farm Business Organization", level300, second_semester),
            ("AEA306", "Farm Records and Accounting", level300, second_semester),
            ("AEA308", "Principles of Farm Management", level300, second_semester),
            ("ANP302", "Introduction to Ruminant Animal Production", level300, second_semester),
            ("ENT310", "Cultural Change and Entrepreneurship", level300, second_semester),
            ("CRP312", "Farm Power and Agricultural Mechanization", level300, second_semester),

            # 400L FIRST SEMESTER
            ("AGR400", "Farm Practical Year / SIWES", level400, first_semester),
            ("AGR401", "Agricultural Industrial Attachment", level400, first_semester),
            ("AGR402", "Farm Enterprise Management Practice", level400, first_semester),
            ("AGR403", "Agribusiness Field Experience", level400, first_semester),

            # 400L SECOND SEMESTER
            ("AGR404", "Continuation of Farm Practical Year / SIWES", level400, second_semester),
            ("AGR405", "Agricultural Enterprise Evaluation", level400, second_semester),
            ("AGR406", "Farm Operations Assessment", level400, second_semester),
            ("AGR407", "Agribusiness Internship Report", level400, second_semester),
            ("AGR408", "Practical Training Documentation", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Agricultural Economics courses."
            )
        )