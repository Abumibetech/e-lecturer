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
    help = "Seed M.Sc. Peace Studies and Conflict Resolution courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Peace Studies and Conflict Resolution"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Sc. Peace Studies and Conflict Resolution"
        )

        courses = {

            (800, "First Semester"): [
                ("PCR811", "Advanced Theories of Conflict"),
                ("PCR813", "Advanced Peace Studies"),
                ("PCR815", "Research Methods in Peace and Conflict Studies"),
                ("PCR817", "Conflict Analysis and Management"),
                ("PCR819", "Peacebuilding and Post-Conflict Reconstruction"),
                ("PCR821", "Mediation, Negotiation and Dialogue"),

                # Electives
                ("PCR823", "Gender, Conflict and Peacebuilding"),
                ("PCR825", "Human Rights and Humanitarian Law"),
                ("PCR827", "Religion, Identity and Conflict"),
            ],

            (800, "Second Semester"): [
                ("PCR812", "Advanced Conflict Resolution Processes"),
                ("PCR814", "Governance, Democracy and Development"),
                ("PCR816", "Security Studies and Strategic Analysis"),
                ("PCR818", "International Peace and Security"),
                ("PCR820", "Early Warning and Conflict Prevention"),
                ("PCR822", "Peacekeeping and International Intervention"),

                # Electives
                ("PCR824", "Terrorism and Counter-Terrorism Studies"),
                ("PCR826", "Migration, Refugees and Human Security"),
                ("PCR828", "Environmental Conflict and Sustainable Development"),
            ],

            (800, "Third Semester"): [
                ("PCR890", "Dissertation Seminar"),
                ("PCR899", "Dissertation / Thesis"),
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
                "M.Sc. Peace Studies and Conflict Resolution courses seeded successfully."
            )
        )