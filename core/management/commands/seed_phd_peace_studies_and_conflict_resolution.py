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
    help = "Seed PhD Peace Studies and Conflict Resolution courses"

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
            name="PhD Peace Studies and Conflict Resolution"
        )

        courses = {

            (900, "First Semester"): [
                ("PCR901", "Advanced Theories of Conflict and Peace"),
                ("PCR903", "Contemporary Issues in Peace and Security Studies"),
                ("PCR905", "Advanced Research Methodology"),
                ("PCR907", "Seminar in Peace and Conflict Studies"),
                ("PCR909", "Advanced Conflict Analysis"),
                ("PCR911", "Peacebuilding and Humanitarian Intervention"),

                # Electives
                ("PCR913", "Ethnic Conflicts and Resolution"),
                ("PCR915", "Arms Control and Demilitarisation"),
                ("PCR917", "Human Rights, Diplomacy and International Peace"),
            ],

            (900, "Second Semester"): [
                ("PCR902", "Political Economy of Peacebuilding"),
                ("PCR904", "International Law, Security and Peace"),
                ("PCR906", "Advanced Conflict Management Systems"),
                ("PCR908", "Governance, Democracy and Sustainable Peace"),
                ("PCR910", "Environmental Security and Conflict Resolution"),
                ("PCR912", "Doctoral Seminar in Peace and Conflict Studies"),

                # Electives
                ("PCR914", "Religion, Identity and Conflict"),
                ("PCR916", "Terrorism and Counter-Terrorism Studies"),
                ("PCR918", "Gender, Security and Peacebuilding"),
            ],

            (900, "Research Stage"): [
                ("PHD991", "PhD Seminar I"),
                ("PHD992", "PhD Seminar II"),
                ("PHD993", "Thesis Proposal Defence"),
                ("PHD999", "Doctoral Thesis"),
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
                "PhD Peace Studies and Conflict Resolution courses seeded successfully."
            )
        )