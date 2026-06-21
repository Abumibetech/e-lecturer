from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Public Health Programme"

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
            name="Public Health",
            defaults={"slug": "public-health"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="BSc Public Health"
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
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # ==================================
            # 200 LEVEL FIRST SEMESTER
            # ==================================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "GST107", "The Good Study Guide"),
            (200, first_semester, "GST101", "Use of English and Communication Skills I"),
            (200, first_semester, "CHM101", "Introduction to Inorganic Chemistry"),
            (200, first_semester, "MTH101", "Elementary Mathematics I"),
            (200, first_semester, "CIT101", "Computers in Society"),
            (200, first_semester, "PHS201", "Anatomy"),
            (200, first_semester, "PHS203", "Introduction to Public Health"),
            (200, first_semester, "PHS217", "General Microbiology"),
            (200, first_semester, "PED221", "Developmental Psychology"),
            (200, first_semester, "PHY103", "Geometric and Wave Optics"),

            # ==================================
            # 200 LEVEL SECOND SEMESTER
            # ==================================
            (200, second_semester, "GST102", "Use of English and Communication Skills II"),
            (200, second_semester, "GST202", "Peace Studies and Conflict Resolution"),
            (200, second_semester, "PHS202", "Human Physiology"),
            (200, second_semester, "PHS204", "Introduction to Biostatistics"),
            (200, second_semester, "PHS206", "Environmental Health"),
            (200, second_semester, "PHS208", "Health Promotion and Education"),
            (200, second_semester, "PHS210", "Introduction to Epidemiology"),
            (200, second_semester, "PHS212", "Demography and Population Studies"),
            (200, second_semester, "PHS401", "Community and Reproductive Adolescent Health"),

            # ==================================
            # 300 LEVEL FIRST SEMESTER
            # ==================================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "PHS301", "Principles of Epidemiology"),
            (300, first_semester, "PHS303", "Environmental and Occupational Health I"),
            (300, first_semester, "PHS305", "Health Behaviour and Health Education"),
            (300, first_semester, "PHS307", "Health Information Systems"),
            (300, first_semester, "PHS309", "Public Health Nutrition"),
            (300, first_semester, "PHS311", "Research Methods in Public Health"),

            # ==================================
            # 300 LEVEL SECOND SEMESTER
            # ==================================
            (300, second_semester, "PHS302", "Biostatistics for Public Health"),
            (300, second_semester, "PHS304", "Environmental and Occupational Health II"),
            (300, second_semester, "PHS306", "Maternal and Child Health"),
            (300, second_semester, "PHS308", "Disease Prevention and Control"),
            (300, second_semester, "PHS310", "Health Planning and Management"),
            (300, second_semester, "PHS312", "Community Health Practice I"),

            # ==================================
            # 400 LEVEL FIRST SEMESTER
            # ==================================
            (400, first_semester, "PHS401", "Public Health Administration"),
            (400, first_semester, "PHS403", "Health Economics"),
            (400, first_semester, "PHS405", "Monitoring and Evaluation of Health Programmes"),
            (400, first_semester, "PHS407", "Reproductive Health"),
            (400, first_semester, "PHS409", "Health Policy and Systems"),
            (400, first_semester, "PHS411", "Advanced Epidemiology"),
            (400, first_semester, "PHS413", "Public Health Research Methods"),
            (400, first_semester, "PHS415", "International Health"),
            (400, first_semester, "PHS417", "Disaster Management and Emergency Preparedness"),

            # ==================================
            # 400 LEVEL SECOND SEMESTER
            # ==================================
            (400, second_semester, "PHS402", "Introduction to Public Health Laws"),
            (400, second_semester, "PHS404", "Occupational Health and Safety"),
            (400, second_semester, "PHS406", "Community Diagnosis"),
            (400, second_semester, "PHS408", "Health Programme Evaluation"),
            (400, second_semester, "PHS426", "Essential Drugs and Public Health Pharmacology"),
            (400, second_semester, "PHS430", "Community Health Practical II"),

            # electives (still stored as courses in your system)
            (400, second_semester, "PHS422", "Clinical Skills I & II"),
            (400, second_semester, "PHS424", "Primary Emergency Obstetrics Care"),
            (400, second_semester, "PHS428", "Rural Health Development"),
            (400, second_semester, "PHS432", "Health Communication Strategies"),

            # ==================================
            # 500 LEVEL FIRST SEMESTER
            # ==================================
            (500, first_semester, "PHS501", "Advanced Public Health Practice"),
            (500, first_semester, "PHS503", "Community Health Management"),
            (500, first_semester, "PHS505", "Community Mental Health"),
            (500, first_semester, "PHS511", "Applied Epidemiology"),
            (500, first_semester, "PHS512", "Seminar in Core Areas of Public Health"),
            (500, first_semester, "PHS507", "Outreach and Mobile Health Services"),
            (500, first_semester, "PHS509", "Geriatrics, Gerontology and Disability Care"),

            # ==================================
            # 500 LEVEL SECOND SEMESTER
            # ==================================
            (500, second_semester, "PHS520", "Community Posting (Internship)"),
            (500, second_semester, "PHS524", "Health Education and Promotion"),
            (500, second_semester, "PHS522", "Research Project"),
            (500, second_semester, "PHS526", "Health Care Financing"),
            (500, second_semester, "PHS528", "Public Health Informatics"),
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
                f"Successfully seeded {created} Public Health courses"
            )
        )