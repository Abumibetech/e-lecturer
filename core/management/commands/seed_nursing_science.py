from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Nursing Science Programme"

    def handle(self, *args, **kwargs):

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Health Sciences",
            defaults={"slug": "health-sciences"}
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Nursing Sciences",
            defaults={"slug": "nursing-sciences"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.NSc. Nursing Science"
        )

        # =========================
        # LEVELS
        # =========================
        level200, _ = Level.objects.get_or_create(name=200)
        level300, _ = Level.objects.get_or_create(name=300)
        level400, _ = Level.objects.get_or_create(name=400)
        level500, _ = Level.objects.get_or_create(name=500)

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
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "NSC201", "Human Anatomy I"),
            (200, first_semester, "NSC203", "Human Physiology I"),
            (200, first_semester, "NSC205", "Introduction to Nursing Theories"),
            (200, first_semester, "NSC207", "Medical-Surgical Nursing I"),
            (200, first_semester, "NSC209", "Nursing Ethics and Law"),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            (200, second_semester, "GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            (200, second_semester, "NSC202", "Human Anatomy II"),
            (200, second_semester, "NSC204", "Human Physiology II"),
            (200, second_semester, "NSC206", "Medical-Surgical Nursing II"),
            (200, second_semester, "NSC208", "Fundamentals of Nursing"),
            (200, second_semester, "NSC210", "Nutrition in Health and Disease"),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            (300, first_semester, "NSC301", "Maternal and Child Health Nursing I"),
            (300, first_semester, "NSC303", "Community Health Nursing I"),
            (300, first_semester, "NSC305", "Medical-Surgical Nursing III"),
            (300, first_semester, "NSC307", "Mental Health Nursing I"),
            (300, first_semester, "NSC309", "Nursing Research Methods"),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            (300, second_semester, "NSC302", "Maternal and Child Health Nursing II"),
            (300, second_semester, "NSC304", "Community Health Nursing II"),
            (300, second_semester, "NSC306", "Medical-Surgical Nursing IV"),
            (300, second_semester, "NSC308", "Mental Health Nursing II"),
            (300, second_semester, "NSC310", "Nursing Education"),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            (400, first_semester, "NSC401", "Nursing Administration and Management I"),
            (400, first_semester, "NSC403", "Medical-Surgical Nursing V"),
            (400, first_semester, "NSC405", "Research Project I"),
            (400, first_semester, "NSC407", "Geriatric Nursing"),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            (400, second_semester, "NSC402", "Nursing Administration and Management II"),
            (400, second_semester, "NSC404", "Medical-Surgical Nursing VI"),
            (400, second_semester, "NSC406", "Research Project II"),
            (400, second_semester, "NSC408", "Advanced Clinical Practice"),

            # ==================================
            # 500 LEVEL FIRST SEMESTER
            # ==================================
            (500, first_semester, "NSC501", "Public-Community Health Nursing III"),
            (500, first_semester, "NSC503", "Advanced Mental Health/Psychiatric Nursing III"),
            (500, first_semester, "NSC505", "Maternal and Child Health III"),
            (500, first_semester, "NSC507", "Seminar in Nursing II"),

            # ==================================
            # 500 LEVEL SECOND SEMESTER
            # ==================================
            (500, second_semester, "NSC502", "Public-Community Health Nursing IV"),
            (500, second_semester, "NSC504", "Monitoring and Evaluation of Health Programmes and Services"),
            (500, second_semester, "NSC506", "Research Project II"),
            (500, second_semester, "NSC508", "Fundamentals of Nursing Informatics"),
        ]

        levels = {
            200: level200,
            300: level300,
            400: level400,
            500: level500,
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
                f"Successfully seeded {created} Nursing Science courses"
            )
        )