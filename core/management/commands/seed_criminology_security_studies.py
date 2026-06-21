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
    help = "Seed B.Sc Criminology and Security Studies"

    def handle(self, *args, **kwargs):

        # ==========================================
        # FACULTY
        # ==========================================
        faculty, _ = Faculty.objects.get_or_create(
            name="Social Sciences"
        )

        # ==========================================
        # DEPARTMENT
        # ==========================================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Criminology and Security Studies"
        )

        # ==========================================
        # PROGRAMME
        # ==========================================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc Criminology and Security Studies"
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
            ("GST101", "Use of English and Communication Skills I", level100, first_semester),
            ("GST105", "History and Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),
            ("CIT101", "Computer in Society", level100, first_semester),
            ("CSS111", "Introduction to Sociology", level100, first_semester),
            ("CSS121", "Introduction to Psychology", level100, first_semester),
            ("CSS133", "Introduction to Criminology I", level100, first_semester),

            # ==================================
            # 100 LEVEL SECOND SEMESTER
            # ==================================
            ("GST102", "Use of English and Communication Skills II", level100, second_semester),
            ("CIT102", "Application Software Skills", level100, second_semester),
            ("CSS112", "Sociology of Law", level100, second_semester),
            ("CSS132", "Ethnography and Social Structure of Nigeria", level100, second_semester),
            ("CSS134", "Geography of Nigeria", level100, second_semester),
            ("CSS136", "Introduction to Criminology II", level100, second_semester),
            ("CSS152", "Introduction to Nigerian Criminal Law", level100, second_semester),

            # ==================================
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            ("CSS211", "Sociology of Crime and Delinquency", level200, first_semester),
            ("CSS241", "Basic Security and Security Threats", level200, first_semester),
            ("CSS243", "Principles of Security Practice and Management", level200, first_semester),
            ("CSS245", "Security Planning, Development and Organization", level200, first_semester),
            ("GST203", "Introduction to Philosophy and Logic", level200, first_semester),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            ("CSS212", "Sociology of Punishment and Corrections", level200, second_semester),
            ("CSS242", "Measurement and Patterns of Crime and Delinquency", level200, second_semester),
            ("CSS244", "Types and Analysis of Security Threats", level200, second_semester),
            ("CSS246", "Legal Framework of Private Security Services in Nigeria", level200, second_semester),
            ("GST202", "Fundamentals of Peace Studies and Conflict Resolution", level200, second_semester),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            ("CSS331", "Methods of Social Research", level300, first_semester),
            ("CSS341", "Policing and Law Enforcement in Nigeria", level300, first_semester),
            ("CSS343", "Information Systems Security Management", level300, first_semester),
            ("CSS351", "Prisons and Correction of Offenders in Nigeria", level300, first_semester),
            ("CSS361", "Juvenile Institutions and Corrections", level300, first_semester),
            ("CSS381", "Domestic Violence", level300, first_semester),
            ("GST302", "Entrepreneurship and Business Creation", level300, first_semester),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            ("CSS342", "Safety Management for Loss Prevention", level300, second_semester),
            ("CSS352", "Theory of Crime and Crime Control", level300, second_semester),
            ("CSS354", "Special Categories of Offenders", level300, second_semester),
            ("CSS356", "Traditional and Informal Crime Control Mechanisms", level300, second_semester),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            ("CSS411", "Contemporary Issues in Criminology", level400, first_semester),
            ("CSS431", "Field Observation", level400, first_semester),
            ("CSS441", "Technical and Electronic Security Systems", level400, first_semester),
            ("CSS443", "Traffic and Road Safety Management", level400, first_semester),
            ("CSS455", "Forensic Science", level400, first_semester),
            ("CSS491", "Emergency, Riot and Disaster Control", level400, first_semester),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            ("CSS433", "Research Project", level400, second_semester),
            ("CSS442", "Professional Ethics in Law Enforcement", level400, second_semester),
            ("CSS452", "Victims of Crime and Human Rights Violations", level400, second_semester),
            ("CSS462", "Criminology II", level400, second_semester),
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
                f"Successfully seeded {len(courses)} Criminology and Security Studies courses."
            )
        )