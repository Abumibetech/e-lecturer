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
    help = "Seed B.A Christian Theology"

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
            name="Religious Studies"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A Christian Theology"
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

            # ==================================
            # 100 LEVEL FIRST SEMESTER
            # ==================================
            ("CRS101", "Introduction to the Study of Islam", level100, first_semester),
            ("CRS111", "Old Testament Survey", level100, first_semester),
            ("CRS113", "Bible Geography", level100, first_semester),
            ("PHL131", "Introduction to Philosophy", level100, first_semester),
            ("CRS141", "Church History I", level100, first_semester),
            ("CRS151", "Religion and Society", level100, first_semester),
            ("CRS173", "Introduction to the Study of Religion", level100, first_semester),
            ("GST101", "Use of English and Communication Skills I", level100, first_semester),
            ("CIT101", "Computers in Society", level100, first_semester),
            ("CRS131", "History and Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),

            # ==================================
            # 100 LEVEL SECOND SEMESTER
            # ==================================
            ("CRS102", "Major Religious Groups in Nigeria", level100, second_semester),
            ("CRS122", "Types of Theology", level100, second_semester),
            ("CRS142", "Church History II", level100, second_semester),
            ("CRS192", "Introduction to African Traditional Religion", level100, second_semester),
            ("CRS152", "Marriage and Family", level100, second_semester),
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("GST104", "Use of Library", level100, second_semester),
            ("POL126", "Citizens and the State", level100, second_semester),

            # ==================================
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            ("CRS211", "Introduction to the Bible", level200, first_semester),
            ("CRS213", "Synoptic Gospels", level200, first_semester),
            ("CRS215", "Greek Grammar", level200, first_semester),
            ("CRS217", "Prophets", level200, first_semester),
            ("CRS231", "Christian Ethics", level200, first_semester),
            ("CRS233", "Philosophy of Religion", level200, first_semester),
            ("CRS261", "Christian Counselling", level200, first_semester),
            ("CRS271", "Christianity in Nigeria", level200, first_semester),
            ("GST201", "Nigerian Peoples and Culture", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            ("CRS202", "Comparative Study of Religions", level200, second_semester),
            ("CRS210", "History and Religion of Israel", level200, second_semester),
            ("CRS212", "Pentateuch", level200, second_semester),
            ("CRS214", "Pauline Epistles", level200, second_semester),
            ("CRS216", "Greek Syntax", level200, second_semester),
            ("CRS218", "Biblical Hermeneutics", level200, second_semester),
            ("CRS222", "Christian Doctrines", level200, second_semester),
            ("CRS272", "Ecumenism", level200, second_semester),
            ("CSS111", "Introduction to Sociology", level200, second_semester),
            ("GST202", "Peace Studies and Conflict Resolution", level200, second_semester),
            ("GST204", "Entrepreneurship and Innovation", level200, second_semester),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            ("CRS311", "Gospel of John", level300, first_semester),
            ("CRS313", "Hebrew Grammar", level300, first_semester),
            ("CRS321", "God and Revelation", level300, first_semester),
            ("CRS323", "Old Testament Theology", level300, first_semester),
            ("CSS351", "Prisons and Correction of Offenders in Nigeria", level300, first_semester),
            ("LAW103", "Introduction to Law", level300, first_semester),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            ("CRS302", "Messianism", level300, second_semester),
            ("CRS314", "Inter-Testamental Literature", level300, second_semester),
            ("CRS316", "Hebrew Syntax", level300, second_semester),
            ("CRS324", "New Testament Theology", level300, second_semester),
            ("CRS352", "Sociology of Religion", level300, second_semester),
            ("GST302", "Business Creation and Growth", level300, second_semester),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            ("CRS423", "Comparative Ethics in a Pluralistic Society", level400, first_semester),
            ("CRS441", "West African Church History", level400, first_semester),
            ("CRS471", "Research Methods", level400, first_semester),
            ("CRS491", "African Traditional Religion and Culture", level400, first_semester),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            ("CRS412", "Gospel of Matthew", level400, second_semester),
            ("CRS422", "Christology", level400, second_semester),
            ("CRS432", "Applied Ethics", level400, second_semester),
            ("CRS472", "Conflict Management", level400, second_semester),
            ("CRS474", "Project", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Christian Theology courses."
            )
        )