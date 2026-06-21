from django.core.management.base import BaseCommand
from core.models import (
    Faculty,
    Department,
    Programme,
    Level,
    Semester,
    Course
)


class Command(BaseCommand):
    help = "Seed B.A. Philosophy Courses"

    def handle(self, *args, **kwargs):

        faculty = Faculty.objects.filter(
            name__icontains="Arts"
        ).first()

        if not faculty:
            self.stdout.write(
                self.style.ERROR(
                    "Faculty of Arts not found."
                )
            )
            return

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Philosophy"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A. Philosophy"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("PHL101", "Introduction to Philosophy"),
                ("PHL103", "Elementary Ethics I"),
                ("PHL105", "Introduction to Logic I"),
                ("PHL107", "Theories of Human Nature"),
                ("PHL131", "Introduction to Philosophy"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Application Software Skills"),
                ("PHL102", "Introduction to African Philosophy"),
                ("PHL104", "Introduction to Philosophical Anthropology"),
                ("PHL106", "Elementary Ethics II"),
                ("PHL108", "Introduction to Logic II"),
                ("POL126", "Citizen and the State"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("PHL201", "Ancient Greek Philosophy"),
                ("PHL203", "Medieval Philosophy"),
                ("PHL205", "Epistemology I"),
                ("PHL207", "Symbolic Logic"),
                ("PHL209", "African Philosophy I"),
                ("PHL211", "Social and Political Philosophy"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("PHL202", "Modern Philosophy"),
                ("PHL204", "Epistemology II"),
                ("PHL206", "Metaphysics I"),
                ("PHL208", "Ethics and Value Theory"),
                ("PHL210", "African Philosophy II"),
                ("PHL212", "Philosophy of Religion"),
            ],

            (300, "First Semester"): [
                ("PHL312", "Existentialism, Hermeneutics and Phenomenology"),
                ("PHL316", "Philosophy of Gender"),
                ("PHL323", "Philosophy of Arts and Literature"),
                ("PHL342", "Early Modern Philosophy"),
                ("PHL362", "Philosophy of Development"),
                ("PHL372", "Research Method in Philosophy"),
            ],

            (300, "Second Semester"): [
                ("PHL305", "Advanced Political Philosophy"),
                ("PHL324", "Cybernetics / Artificial Intelligence"),
                ("PHL332", "Philosophy of Language"),
                ("PHL334", "Philosophy of Mind"),
                ("PHL352", "Environmental Philosophy"),
                ("GST302", "Entrepreneurship and Innovation"),
            ],

            (400, "First Semester"): [
                ("PHL411", "Contemporary African Philosophy"),
                ("PHL413", "Metaphysical Anthropology"),
                ("PHL415", "Philosophy of History"),
                ("PHL433", "Philosophy of Science"),
                ("PHL451", "Seminar in Philosophy"),
                ("PHL499", "Research Project I"),
            ],

            (400, "Second Semester"): [
                ("PHL423", "Comparative Ethics in Pluralistic Society"),
                ("PHL431", "Further Logic"),
                ("PHL432", "Applied Ethics"),
                ("PHL442", "Modern Philosophy"),
                ("PHL454", "Advanced Philosophy of Religion"),
                ("PHL462", "Philosophy of Law"),
                ("PHL498", "Research Project II"),
            ],
        }

        total = 0

        for (level_num, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=level_num
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
                        "description": f"{title} ({code})"
                    }
                )

                total += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {total} Philosophy courses."
            )
        )