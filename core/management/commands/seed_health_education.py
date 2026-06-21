from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Health Education Programme"

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
            name="Health Education"
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
            (100, first_semester, "HED101", "Introduction to Health Education"),
            (100, first_semester, "HED103", "Foundations of Health Education"),
            (100, first_semester, "KHE101", "Introduction to Human Kinetics"),

            # ==================================
            # 100 LEVEL SECOND SEMESTER
            # ==================================
            (100, second_semester, "GST102", "Use of English and Communication Skills II"),
            (100, second_semester, "EDU112", "Professionalism in Teaching"),
            (100, second_semester, "EDU114", "History of Education"),
            (100, second_semester, "BIO102", "General Biology II"),
            (100, second_semester, "BIO192", "General Practical Biology II"),
            (100, second_semester, "HED102", "Human Anatomy and Physiology"),
            (100, second_semester, "HED104", "Personal Health"),
            (100, second_semester, "HED106", "Community Health"),
            (100, second_semester, "KHE102", "Human Movement Studies"),

            # ==================================
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "EDU231", "Curriculum Theory and Practice"),
            (200, first_semester, "EDU233", "General Teaching Methods"),
            (200, first_semester, "HED201", "School Health Programme"),
            (200, first_semester, "HED203", "Environmental Health"),
            (200, first_semester, "HED205", "Human Nutrition"),
            (200, first_semester, "HED207", "Communicable and Non-Communicable Diseases"),
            (200, first_semester, "HED209", "Mental and Emotional Health"),
            (200, first_semester, "HED281", "Health Education Methods I"),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            (200, second_semester, "GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            (200, second_semester, "EDU212", "Sociology of Education"),
            (200, second_semester, "EDU214", "Philosophy of Education"),
            (200, second_semester, "HED202", "Family Life and Reproductive Health"),
            (200, second_semester, "HED204", "Consumer Health Education"),
            (200, second_semester, "HED206", "Safety Education"),
            (200, second_semester, "HED208", "Drug Use, Abuse and Prevention"),
            (200, second_semester, "HED210", "Epidemiology and Disease Prevention"),
            (200, second_semester, "HED282", "Health Education Methods II"),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "EDU321", "Psychology of Learning"),
            (300, first_semester, "EDU323", "Basic Research Methods in Education"),
            (300, first_semester, "EDU335", "Teaching Practice I"),
            (300, first_semester, "HED301", "Public Health Education"),
            (300, first_semester, "HED303", "Health Promotion Strategies"),
            (300, first_semester, "HED305", "Health Communication"),
            (300, first_semester, "HED307", "Health Counselling"),
            (300, first_semester, "HED309", "First Aid and Safety Education"),
            (300, first_semester, "HED381", "Curriculum Development in Health Education"),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            (300, second_semester, "EDU300", "SIWES"),
            (300, second_semester, "EDU314", "Comparative Education"),
            (300, second_semester, "EDU332", "Educational Technology"),
            (300, second_semester, "EDU336", "Teaching Practice Evaluation and Feedback"),
            (300, second_semester, "HED302", "Community Health Practice"),
            (300, second_semester, "HED304", "Health Education Materials and Media"),
            (300, second_semester, "HED306", "Research Methods in Health Education"),
            (300, second_semester, "HED308", "School Health Services"),
            (300, second_semester, "HED382", "Evaluation in Health Education"),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            (400, first_semester, "EDU421", "Guidance and Counselling"),
            (400, first_semester, "EDU423", "Measurement and Evaluation"),
            (400, first_semester, "EDU435", "Teaching Practice II"),
            (400, first_semester, "HED401", "Contemporary Issues in Health Education"),
            (400, first_semester, "HED403", "Health Behaviour and Behaviour Modification"),
            (400, first_semester, "HED405", "Maternal and Child Health"),
            (400, first_semester, "HED407", "Occupational Health"),
            (400, first_semester, "HED409", "Seminar in Health Education"),
            (400, first_semester, "HED434", "Supervision of School Health Programme"),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            (400, second_semester, "EDU412", "Principles of Educational Management"),
            (400, second_semester, "EDU420", "Research Project"),
            (400, second_semester, "EDU426", "Special Education"),
            (400, second_semester, "HED402", "Health Programme Planning"),
            (400, second_semester, "HED404", "Community Health Development"),
            (400, second_semester, "HED406", "Health Administration and Management"),
            (400, second_semester, "HED408", "Global Health Issues"),
            (400, second_semester, "HED499", "Project in Health Education"),
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
                f"Successfully seeded {created} Health Education courses"
            )
        )