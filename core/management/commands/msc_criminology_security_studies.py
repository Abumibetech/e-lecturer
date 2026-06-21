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
    help = "Seed M.Sc. Criminology and Security Studies courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Criminology and Security Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Sc. Criminology and Security Studies"
        )

        courses = {

            (800, "First Semester"): [
                ("CSS801", "Advanced Criminological Theory"),
                ("CSS803", "Advanced Research Methods"),
                ("CSS805", "Comparative Criminal Justice Systems"),
                ("CSS807", "Advanced Security Studies"),
                ("CSS809", "Contemporary Issues in Criminology and Security"),
                ("CSS811", "Intelligence and Security Management"),

                # Electives
                ("CSS813", "Organized Crime and Transnational Criminal Networks"),
                ("CSS815", "Terrorism and Counter-Terrorism Studies"),
                ("CSS817", "Policing and Law Enforcement Administration"),
            ],

            (800, "Second Semester"): [
                ("CSS802", "Advanced Crime Prevention and Control"),
                ("CSS804", "Social Policy, Juvenile Delinquency and Criminal Justice"),
                ("CSS806", "International Security and Strategic Studies"),
                ("CSS808", "Advanced Cybercrimes and Cyber Security"),
                ("CSS810", "Cybercrime and Forensic Investigation"),
                ("CSS830", "Victimology and Crime Statistics"),

                # Electives
                ("CSS812", "Cybercrimes"),
                ("CSS814", "Corrections and Penal Administration"),
                ("CSS816", "Human Rights and Criminal Justice"),
            ],

            (800, "Third Semester"): [
                ("CSS890", "Dissertation Seminar"),
                ("CSS899", "Thesis / Dissertation"),
            ],
        }

        for (level_number, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=level_number
            )

            semester, _ = Semester.objects.get_or_create(
                name=semester_name
            )

            for code, title in course_list:

                Course.objects.get_or_create(
                    programme=programme,
                    code=code,
                    defaults={
                        "title": title,
                        "level": level,
                        "semester": semester,
                    }
                )

        self.stdout.write(
            self.style.SUCCESS(
                "M.Sc. Criminology and Security Studies courses seeded successfully."
            )
        )