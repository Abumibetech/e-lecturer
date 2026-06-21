from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Human Kinetics Programme"

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
            name="Health and Human Kinetics Education",
            defaults={"slug": "health-and-human-kinetics-education"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Human Kinetics"
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

            # ==================================
            # 100 LEVEL FIRST SEMESTER
            # ==================================
            (100, first_semester, "GST101", "Use of English and Communication Skills I"),
            (100, first_semester, "GST105", "History and Philosophy of Science"),
            (100, first_semester, "GST107", "The Good Study Guide"),
            (100, first_semester, "CIT101", "Computers in Society"),
            (100, first_semester, "EDU111", "Introduction to Foundations of Education"),
            (100, first_semester, "BIO101", "General Biology I"),
            (100, first_semester, "BIO191", "General Practical Biology I"),
            (100, first_semester, "KHE101", "Introduction to Human Kinetics"),
            (100, first_semester, "KHE103", "History and Philosophy of Physical Education"),
            (100, first_semester, "KHE105", "Organization and Administration of Sports"),

            # ==================================
            # 100 LEVEL SECOND SEMESTER
            # ==================================
            (100, second_semester, "GST102", "Use of English and Communication Skills II"),
            (100, second_semester, "EDU112", "Professionalism in Teaching"),
            (100, second_semester, "EDU114", "History of Education"),
            (100, second_semester, "BIO102", "General Biology II"),
            (100, second_semester, "BIO192", "General Practical Biology II"),
            (100, second_semester, "KHE102", "Human Movement Studies"),
            (100, second_semester, "KHE104", "Recreation and Leisure Studies"),
            (100, second_semester, "KHE106", "Introduction to Athletics"),
            (100, second_semester, "HED102", "Human Anatomy and Physiology"),

            # ==================================
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "EDU231", "Curriculum Theory and Practice"),
            (200, first_semester, "EDU233", "General Teaching Methods"),
            (200, first_semester, "KHE201", "Foundations of Exercise Physiology"),
            (200, first_semester, "KHE203", "Sports Psychology"),
            (200, first_semester, "KHE205", "Sociology of Sports"),
            (200, first_semester, "KHE207", "Sports Coaching Theory"),
            (200, first_semester, "KHE209", "Organization and Administration of Physical Education"),
            (200, first_semester, "KHE281", "Human Kinetics Methods I"),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            (200, second_semester, "GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            (200, second_semester, "EDU212", "Sociology of Education"),
            (200, second_semester, "EDU214", "Philosophy of Education"),
            (200, second_semester, "KHE202", "Biomechanics and Kinesiology"),
            (200, second_semester, "KHE204", "Sports Officiating"),
            (200, second_semester, "KHE206", "Adapted Physical Education"),
            (200, second_semester, "KHE208", "Tests, Measurement and Evaluation in Physical Education"),
            (200, second_semester, "KHE210", "Sports Injuries and Rehabilitation"),
            (200, second_semester, "KHE282", "Human Kinetics Methods II"),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "EDU321", "Psychology of Learning"),
            (300, first_semester, "EDU323", "Basic Research Methods in Education"),
            (300, first_semester, "EDU335", "Teaching Practice I"),
            (300, first_semester, "KHE301", "Advanced Exercise Physiology"),
            (300, first_semester, "KHE303", "Motor Learning and Performance"),
            (300, first_semester, "KHE305", "Sports Management"),
            (300, first_semester, "KHE307", "Sports Nutrition"),
            (300, first_semester, "KHE309", "Recreation Programming"),
            (300, first_semester, "KHE381", "Curriculum Development in Human Kinetics"),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            (300, second_semester, "EDU300", "SIWES"),
            (300, second_semester, "EDU314", "Comparative Education"),
            (300, second_semester, "EDU332", "Educational Technology"),
            (300, second_semester, "EDU336", "Teaching Practice Evaluation and Feedback"),
            (300, second_semester, "KHE302", "Sports Medicine"),
            (300, second_semester, "KHE304", "Sports Marketing and Promotion"),
            (300, second_semester, "KHE306", "Research Methods in Human Kinetics"),
            (300, second_semester, "KHE308", "Facility Planning and Management"),
            (300, second_semester, "KHE382", "Evaluation in Human Kinetics"),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            (400, first_semester, "EDU421", "Guidance and Counselling"),
            (400, first_semester, "EDU423", "Measurement and Evaluation"),
            (400, first_semester, "EDU435", "Teaching Practice II"),
            (400, first_semester, "KHE401", "Contemporary Issues in Human Kinetics"),
            (400, first_semester, "KHE403", "Sports and Society"),
            (400, first_semester, "KHE405", "Advanced Coaching Techniques"),
            (400, first_semester, "KHE407", "Sports Administration"),
            (400, first_semester, "KHE409", "Seminar in Human Kinetics"),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            (400, second_semester, "EDU412", "Principles of Educational Management"),
            (400, second_semester, "EDU420", "Research Project"),
            (400, second_semester, "EDU426", "Special Education"),
            (400, second_semester, "KHE402", "Sports Policy and Development"),
            (400, second_semester, "KHE404", "Sports Entrepreneurship"),
            (400, second_semester, "KHE406", "Health and Fitness Education"),
            (400, second_semester, "KHE408", "Recreation and Tourism Management"),
            (400, second_semester, "KHE499", "Project in Human Kinetics"),
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
                f"Successfully seeded {created} Human Kinetics courses"
            )
        )