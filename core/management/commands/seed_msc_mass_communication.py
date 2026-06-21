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
    help = "Seed M.Sc. Mass Communication courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Communication and Media Studies"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mass Communication"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Sc. Mass Communication"
        )

        courses = {

            (800, "First Semester"): [
                ("MAC811", "Advanced Communication Theory"),
                ("MAC813", "Advanced Research Methods in Mass Communication"),
                ("MAC815", "Media, Culture and Society"),
                ("MAC817", "Advanced Journalism Studies"),
                ("MAC819", "Advanced Broadcasting Studies"),
                ("MAC821", "Development Communication"),

                # Electives
                ("MAC823", "International Communication"),
                ("MAC825", "Political Communication"),
                ("MAC827", "Health Communication"),
            ],

            (800, "Second Semester"): [
                ("MAC812", "Communication Models and Analysis"),
                ("MAC814", "Quantitative and Qualitative Communication Research"),
                ("MAC816", "Media Law, Ethics and Regulation"),
                ("MAC818", "Public Relations Theory and Practice"),
                ("MAC820", "Advertising and Integrated Marketing Communication"),
                ("MAC822", "New Media Technologies and Digital Communication"),

                # Electives
                ("MAC824", "Corporate Communication"),
                ("MAC826", "Crisis Communication"),
                ("MAC828", "Environmental Communication"),
            ],

            (800, "Third Semester"): [
                ("MAC890", "Dissertation Seminar"),
                ("MAC899", "Thesis / Dissertation"),
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
                "M.Sc. Mass Communication courses seeded successfully."
            )
        )