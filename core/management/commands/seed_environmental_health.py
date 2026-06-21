from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Environmental Health Science Programme"

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
            name="Environmental Health Science",
            defaults={"slug": "environmental-health-science"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Environmental Health Science"
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

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, first_semester, "GST201", "Nigerian Peoples and Culture"),
            (200, first_semester, "GST203", "Introduction to Philosophy and Logic"),
            (200, first_semester, "CHM101", "Introduction to Inorganic Chemistry"),
            (200, first_semester, "MTH101", "Elementary Mathematics I"),
            (200, first_semester, "CIT101", "Computers in Society"),
            (200, first_semester, "BIO101", "General Biology I"),
            (200, first_semester, "EHS201", "Introduction to Environmental Health Science"),
            (200, first_semester, "EHS203", "Human Anatomy and Physiology"),
            (200, first_semester, "EHS205", "Environmental Chemistry"),
            (200, first_semester, "EHS207", "Introduction to Epidemiology"),
            (200, first_semester, "EHS209", "Community Health Principles"),

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, second_semester, "GST202", "Peace Studies and Conflict Resolution"),
            (200, second_semester, "BIO102", "General Biology II"),
            (200, second_semester, "EHS202", "Environmental Sanitation"),
            (200, second_semester, "EHS204", "Waste Management and Control"),
            (200, second_semester, "EHS206", "Public Health Microbiology"),
            (200, second_semester, "EHS208", "Introduction to Occupational Health"),
            (200, second_semester, "EHS210", "Environmental Pollution and Control"),

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, first_semester, "GST301", "Entrepreneurship Studies"),
            (300, first_semester, "EHS301", "Principles of Environmental Health Practice"),
            (300, first_semester, "EHS303", "Environmental Toxicology"),
            (300, first_semester, "EHS305", "Food Safety and Hygiene"),
            (300, first_semester, "EHS307", "Water Supply and Sanitation"),
            (300, first_semester, "EHS309", "Environmental Health Law and Policy"),
            (300, first_semester, "EHS311", "Research Methods in Environmental Health"),

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, second_semester, "EHS302", "Environmental Risk Assessment"),
            (300, second_semester, "EHS304", "Air and Noise Pollution Control"),
            (300, second_semester, "EHS306", "Solid and Hazardous Waste Management"),
            (300, second_semester, "EHS308", "Occupational Health and Safety Management"),
            (300, second_semester, "EHS310", "Vector Control and Disease Prevention"),
            (300, second_semester, "EHS312", "Community Environmental Health Practice I"),

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, first_semester, "EHS401", "Environmental Health Management"),
            (400, first_semester, "EHS403", "Industrial Hygiene"),
            (400, first_semester, "EHS405", "Environmental Epidemiology"),
            (400, first_semester, "EHS407", "Climate Change and Health"),
            (400, first_semester, "EHS409", "Environmental Health Policy and Planning"),
            (400, first_semester, "EHS411", "Monitoring and Evaluation of Environmental Programs"),
            (400, first_semester, "EHS413", "Environmental Impact Assessment"),

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, second_semester, "EHS402", "Environmental Health Legislation and Enforcement"),
            (400, second_semester, "EHS404", "Disaster Risk Management and Emergency Response"),
            (400, second_semester, "EHS406", "Rural and Urban Environmental Health"),
            (400, second_semester, "EHS408", "Environmental Health Inspection Techniques"),
            (400, second_semester, "EHS410", "Community Environmental Health Practice II"),
            (400, second_semester, "EHS412", "Industrial Pollution Control and Management"),

            # =========================
            # 500 LEVEL FIRST SEMESTER
            # =========================
            (500, first_semester, "EHS501", "Advanced Environmental Health Practice"),
            (500, first_semester, "EHS503", "Environmental Health Administration"),
            (500, first_semester, "EHS505", "Occupational Disease Control"),
            (500, first_semester, "EHS507", "Environmental Impact Assessment Practicum"),
            (500, first_semester, "EHS509", "Disaster Risk and Emergency Environmental Response"),
            (500, first_semester, "EHS511", "Advanced Environmental Epidemiology"),
            (500, first_semester, "EHS513", "Seminar in Environmental Health Science"),

            # =========================
            # 500 LEVEL SECOND SEMESTER
            # =========================
            (500, second_semester, "EHS520", "Community Environmental Health Posting"),
            (500, second_semester, "EHS522", "Research Project in Environmental Health Science"),
            (500, second_semester, "EHS524", "Environmental Health Policy Analysis"),
            (500, second_semester, "EHS526", "Climate Change Mitigation Strategies"),
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
                f"Successfully seeded {created} Environmental Health Science courses"
            )
        )