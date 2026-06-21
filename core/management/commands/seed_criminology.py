from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed Criminology & Security Studies (100L - 400L)"

    def handle(self, *args, **kwargs):

        # =========================
        # LEVELS
        # =========================
        levels = {}
        for i in range(100, 500, 100):
            levels[i], _ = Level.objects.get_or_create(name=i)

        # =========================
        # SEMESTERS
        # =========================
        sem1, _ = Semester.objects.get_or_create(name="First Semester")
        sem2, _ = Semester.objects.get_or_create(name="Second Semester")

        # =========================
        # FACULTY / DEPARTMENT / PROGRAMME
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="FACULTY OF SOCIAL SCIENCES"
        )

        department, _ = Department.objects.get_or_create(
            name="Department of Criminology and Security Studies",
            faculty=faculty
        )

        programme, _ = Programme.objects.get_or_create(
            name="Criminology and Security Studies",
            department=department
        )

        # =========================
        # FULL COURSE STRUCTURE
        # =========================
        data = {
            100: {
                sem1: [
                    ("GST101", "Use of English and Communication Skills I"),
                    ("GST105", "History and Philosophy of Science"),
                    ("GST107", "The Good Study Guide"),
                    ("CSS111", "Introduction to Sociology"),
                    ("CSS121", "Introduction to Psychology"),
                    ("CSS133", "Introduction to Criminology I"),
                    ("CIT101", "Computer in Society"),
                ],
                sem2: [
                    ("GST102", "Use of English and Communication Skills II"),
                    ("CSS112", "Sociology of Law"),
                    ("CSS132", "Ethnography and Social Structure of Nigeria"),
                    ("CSS134", "Geography of Nigeria"),
                    ("CSS136", "Introduction to Criminology II"),
                    ("CSS152", "Introduction to Nigerian Criminal Law"),
                    ("CIT102", "Application Software Skills"),
                ]
            },

            200: {
                sem1: [
                    ("CSS211", "Sociology of Crime and Delinquency"),
                    ("CSS241", "Basic Security and Security Threats"),
                    ("CSS243", "Principles of Security Practice"),
                    ("CSS245", "Security Planning and Management"),
                ],
                sem2: [
                    ("CSS212", "Sociology of Punishment"),
                    ("CSS242", "Crime Measurement and Patterns"),
                    ("CSS244", "Security Threat Analysis"),
                    ("CSS246", "Legal Framework of Private Security"),
                ]
            },

            300: {
                sem1: [
                    ("CSS331", "Methods of Social Research"),
                    ("CSS341", "Policing and Law Enforcement"),
                    ("CSS343", "Information Security Management"),
                    ("CSS351", "Correctional Institutions"),
                    ("CSS381", "Domestic Violence Studies"),
                ],
                sem2: [
                    ("CSS342", "Safety Management"),
                    ("CSS352", "Theory of Crime"),
                    ("CSS354", "Special Offenders"),
                    ("CSS356", "Informal Crime Control"),
                ]
            },

            400: {
                sem1: [
                    ("CSS411", "Contemporary Criminology"),
                    ("CSS441", "Electronic Security Systems"),
                    ("CSS443", "Traffic Safety Management"),
                    ("CSS455", "Forensic Science"),
                    ("CSS491", "Emergency & Disaster Control"),
                ],
                sem2: [
                    ("CSS433", "Research Project"),
                    ("CSS442", "Professional Ethics"),
                    ("CSS452", "Victims of Crime"),
                    ("CSS462", "Advanced Criminology"),
                ]
            }
        }

        # =========================
        # SEED COURSES
        # =========================
        created = 0

        for level_value, semesters in data.items():
            level = levels[level_value]

            for semester, courses in semesters.items():

                for code, title in courses:

                    Course.objects.get_or_create(
                        programme=programme,
                        level=level,
                        semester=semester,
                        code=code,
                        title=title,
                    )

                    created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Criminology Seed Completed → {created} courses created"
        ))