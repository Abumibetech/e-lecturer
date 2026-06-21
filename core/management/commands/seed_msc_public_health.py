from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed M.Sc Public Health Programme"

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
            name="M.Sc Public Health"
        )

        # =========================
        # LEVEL
        # =========================
        level, _ = Level.objects.get_or_create(name=800)

        # =========================
        # SEMESTERS
        # =========================
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # =========================
            # FIRST SEMESTER
            # =========================
            (800, first_semester, "GST807", "The Good Study Guide (Postgraduate Level)"),
            (800, first_semester, "PHS801", "Advanced Principles of Epidemiology"),
            (800, first_semester, "PHS803", "Advanced Biostatistics for Public Health"),
            (800, first_semester, "PHS805", "Health Policy and Systems Analysis"),
            (800, first_semester, "PHS807", "Environmental and Occupational Health (Advanced)"),
            (800, first_semester, "PHS809", "Research Methods in Public Health"),
            (800, first_semester, "PHS811", "Health Promotion and Behavioural Science"),
            (800, first_semester, "PHS813", "Seminar in Public Health Studies I"),

            # =========================
            # SECOND SEMESTER
            # =========================
            (800, second_semester, "PHS802", "Advanced Disease Prevention and Control"),
            (800, second_semester, "PHS804", "Health Economics and Financing"),
            (800, second_semester, "PHS806", "Global Health and Development"),
            (800, second_semester, "PHS808", "Public Health Surveillance Systems"),
            (800, second_semester, "PHS810", "Monitoring and Evaluation of Health Programmes"),
            (800, second_semester, "PHS812", "Health Informatics and Data Systems"),
            (800, second_semester, "PHS814", "Seminar in Public Health Studies II"),

            # =========================
            # ELECTIVES
            # =========================
            (800, first_semester, "PHS815", "Disaster Risk Reduction and Emergency Health Management"),
            (800, first_semester, "PHS817", "Advanced Environmental Health and Toxicology"),
            (800, first_semester, "PHS819", "Maternal and Child Health in Developing Countries"),
            (800, first_semester, "PHS821", "Mental Health and Community Interventions"),
            (800, first_semester, "PHS823", "Infectious Disease Modelling and Control"),

            # =========================
            # RESEARCH COMPONENT
            # =========================
            (800, second_semester, "PHS899", "Dissertation (M.Sc. Public Health Research Project)"),
        ]

        created = 0

        for level_num, semester, code, title in courses:
            _, was_created = Course.objects.get_or_create(
                programme=programme,
                level=level,
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
                f"Successfully seeded {created} M.Sc Public Health courses"
            )
        )