from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Library and Information Science Programme"

    def handle(self, *args, **kwargs):

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Education",
            defaults={"slug": "education"}
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Library and Information Science",
            defaults={"slug": "library-and-information-science"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Library and Information Science"
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
        first_semester, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        second_semester, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        courses = [

            # =========================
            # 100L FIRST SEMESTER
            # =========================
            (100, first_semester, "GST101", "Use of English and Communication Skills I"),
            (100, first_semester, "GST105", "History and Philosophy of Science"),
            (100, first_semester, "GST107", "The Good Study Guide"),
            (100, first_semester, "CIT101", "Computers in Society"),
            (100, first_semester, "LIS101", "Historical Foundations of Libraries and Information Centres"),
            (100, first_semester, "LIS103", "Introduction to Library and Information Work"),
            (100, first_semester, "LIS105", "Libraries and Societal Development"),
            (100, first_semester, "EDU111", "Introduction to Foundations of Education"),

            # =========================
            # 100L SECOND SEMESTER
            # =========================
            (100, second_semester, "GST102", "Use of English and Communication Skills II"),
            (100, second_semester, "EDU112", "Professionalism in Teaching"),
            (100, second_semester, "EDU114", "History of Education"),
            (100, second_semester, "LIS112", "Library and Information Centres Visits"),
            (100, second_semester, "LIS114", "Book Production Processes and Publishing"),
            (100, second_semester, "LIS116", "Information Literacy"),
            (100, second_semester, "LIS118", "Types of Libraries"),
            (100, second_semester, "CIT102", "Software Application Skills"),

            # =========================
            # 200L FIRST SEMESTER
            # =========================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "LIS201", "Introduction to Bibliography"),
            (200, first_semester, "LIS203", "Cataloguing and Classification I"),
            (200, first_semester, "LIS205", "Collection Development"),
            (200, first_semester, "LIS207", "Reference and Information Services"),
            (200, first_semester, "LIS209", "Information Sources and Services"),
            (200, first_semester, "LIS211", "Library Use Studies"),

            # =========================
            # 200L SECOND SEMESTER
            # =========================
            (200, second_semester, "GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            (200, second_semester, "LIS202", "Indexing and Abstracting"),
            (200, second_semester, "LIS204", "Information Storage and Retrieval"),
            (200, second_semester, "LIS206", "Records and Archives Management I"),
            (200, second_semester, "LIS208", "Publishing and Media Resources"),
            (200, second_semester, "LIS210", "Computer Applications in Library and Information Science"),
            (200, second_semester, "LIS212", "Library Administration and Management"),

            # =========================
            # 300L FIRST SEMESTER
            # =========================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "LIS301", "Cataloguing and Classification II"),
            (300, first_semester, "LIS303", "Information Retrieval (Cataloguing II)"),
            (300, first_semester, "LIS305", "Digital Libraries"),
            (300, first_semester, "LIS307", "Information Storage and Retrieval Systems"),
            (300, first_semester, "LIS309", "School Library Services"),
            (300, first_semester, "LIS311", "Research Methods in Library and Information Science"),
            (300, first_semester, "LIS313", "Database Management Systems"),

            # =========================
            # 300L SECOND SEMESTER
            # =========================
            (300, second_semester, "LIS302", "Library Automation"),
            (300, second_semester, "LIS304", "Records and Archives Management II"),
            (300, second_semester, "LIS306", "Information Technology Applications in Libraries"),
            (300, second_semester, "LIS308", "Library Management"),
            (300, second_semester, "LIS321", "Management and Use of Government Publications"),
            (300, second_semester, "LIS327", "Introduction to Computer Operating System"),
            (300, second_semester, "LIS390", "SIWES"),

            # =========================
            # 400L FIRST SEMESTER
            # =========================
            (400, first_semester, "LIS401", "Knowledge Management"),
            (400, first_semester, "LIS403", "Information Seeking Behaviour"),
            (400, first_semester, "LIS405", "Advanced Reference and Information Services"),
            (400, first_semester, "LIS407", "Preservation and Conservation of Information Materials"),
            (400, first_semester, "LIS409", "Information Systems Analysis and Design"),
            (400, first_semester, "LIS415", "Information Resources in Subject Areas"),
            (400, first_semester, "LIS417", "Research Seminar"),

            # =========================
            # 400L SECOND SEMESTER
            # =========================
            (400, second_semester, "LIS402", "Special Libraries and Information Centres"),
            (400, second_semester, "LIS404", "Information Literacy and User Education"),
            (400, second_semester, "LIS406", "Library Networking and Resource Sharing"),
            (400, second_semester, "LIS408", "Information Policy and Analysis"),
            (400, second_semester, "LIS410", "Project"),
            (400, second_semester, "LIS416", "Introduction to Digital Information Systems and Services"),
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
                f"Successfully seeded {created} Library and Information Science courses"
            )
        )