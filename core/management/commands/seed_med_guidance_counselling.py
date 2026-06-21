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
    help = "Seed M.Ed Guidance and Counselling courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Guidance and Counselling"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="M.Ed. Guidance and Counselling"
        )

        courses = {

            # =========================
            # 800 LEVEL FIRST SEMESTER
            # =========================
            (800, "First Semester"): [

                ("GST807", "The Good Study Guide"),
                ("EGC801", "Principles of Guidance and Counselling"),
                ("EGC803", "Developmental Psychology"),
                ("EGC805", "Vocational Guidance"),
                ("EGC809", "Psychological Testing"),
                ("EDU821", "Statistical Methods"),
                ("EDU823", "Educational Research Methods"),
                ("CIT101", "Computers in Society"),
            ],

            # ==========================
            # 800 LEVEL SECOND SEMESTER
            # ==========================
            (800, "Second Semester"): [

                ("EGC802", "Counselling Theories"),
                ("EGC804", "Techniques of Counselling"),
                ("EGC806", "Organization and Administration of Guidance Services"),
                ("EGC810", "Graduate Seminar"),
                ("EGC812", "Behaviour Modification"),
            ],

            # =========================
            # 800 LEVEL THIRD SEMESTER
            # =========================
            (800, "Third Semester"): [

                ("EGC811", "Principles of Interpersonal Relationships"),
                ("EGC813", "Group Dynamics"),
                ("EGC815", "Sex and Family Counselling"),
                ("EGC817", "Abnormal Psychology"),
            ],

            # ==========================
            # 800 LEVEL FOURTH SEMESTER
            # ==========================
            (800, "Fourth Semester"): [

                ("EGC814", "Practicum and Directed Field Exposure"),
                ("EDU820", "Research Project"),
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
                "M.Ed Guidance and Counselling courses seeded successfully."
            )
        )