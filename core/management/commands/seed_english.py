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
    help = "Seed NOUN English Programme"

    def handle(self, *args, **kwargs):

        # ==========================
        # FACULTY
        # ==========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Arts"
        )

        # ==========================
        # DEPARTMENT
        # ==========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="English"
        )

        # ==========================
        # PROGRAMME
        # ==========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="English"
        )

        # ==========================
        # LEVELS
        # ==========================
        level100, _ = Level.objects.get_or_create(name=100)
        level200, _ = Level.objects.get_or_create(name=200)
        level300, _ = Level.objects.get_or_create(name=300)
        level400, _ = Level.objects.get_or_create(name=400)

        # ==========================
        # SEMESTERS
        # ==========================
        first_semester, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        second_semester, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        # ==========================
        # COURSES
        # ==========================
        courses = [

            # 100L FIRST SEMESTER
            ("GST101", "Use of English & Communication Skills I", level100, first_semester),
            ("GST105", "History & Philosophy of Science", level100, first_semester),
            ("GST107", "The Good Study Guide", level100, first_semester),
            ("CIT101", "Computer in Society", level100, first_semester),
            ("ENG113", "Introduction to Nigerian Literature I", level100, first_semester),
            ("ENG121", "Structure of Modern English I", level100, first_semester),
            ("ENG141", "Spoken English", level100, first_semester),
            ("ENG161", "Theatre Workshop", level100, first_semester),
            ("ENG181", "Introduction to Prose Fiction", level100, first_semester),

            # 100L SECOND SEMESTER
            ("GST102", "Use of English & Communication Skills II", level100, second_semester),
            ("CIT102", "Application Software Skills", level100, second_semester),
            ("ENG114", "Introduction to Nigerian Literature II", level100, second_semester),
            ("ENG122", "Structure of Modern English II", level100, second_semester),
            ("ENG151", "Introduction to English as a Second Language", level100, second_semester),
            ("ENG162", "Elements of Drama", level100, second_semester),
            ("ENG172", "Introduction to Poetry", level100, second_semester),

            # 200L FIRST SEMESTER
            ("ENG211", "English Language and Communication Skills", level200, first_semester),
            ("ENG221", "English Syntax", level200, first_semester),
            ("ENG231", "Introduction to Semantics", level200, first_semester),
            ("ENG241", "Phonetics and Phonology", level200, first_semester),
            ("ENG251", "African Oral Literature", level200, first_semester),
            ("ENG261", "Introduction to Literary Theory", level200, first_semester),
            ("ENG271", "English Language in Nigeria", level200, first_semester),

            # 200L SECOND SEMESTER
            ("ENG212", "Advanced English Composition", level200, second_semester),
            ("ENG222", "English Morphology", level200, second_semester),
            ("ENG232", "Introduction to Pragmatics", level200, second_semester),
            ("ENG242", "English Phonology", level200, second_semester),
            ("ENG252", "African Written Literature", level200, second_semester),
            ("ENG262", "Literary Appreciation and Criticism", level200, second_semester),
            ("ENG272", "Varieties of English", level200, second_semester),

            # 300L FIRST SEMESTER
            ("ENG311", "History of the English Language", level300, first_semester),
            ("ENG321", "Introduction to Discourse Analysis", level300, first_semester),
            ("ENG331", "Stylistics", level300, first_semester),
            ("ENG341", "Sociolinguistics", level300, first_semester),
            ("ENG351", "English for Specific Purposes", level300, first_semester),
            ("ENG361", "Nigerian Literature in English", level300, first_semester),
            ("ENG371", "Shakespearean Drama", level300, first_semester),
            ("ENG381", "Modern African Poetry", level300, first_semester),

            # 300L SECOND SEMESTER
            ("ENG312", "Language and Communication", level300, second_semester),
            ("ENG322", "Semantics and Pragmatics", level300, second_semester),
            ("ENG332", "Advanced Stylistics", level300, second_semester),
            ("ENG342", "Psycholinguistics", level300, second_semester),
            ("ENG352", "Applied Linguistics", level300, second_semester),
            ("ENG362", "Commonwealth Literature", level300, second_semester),
            ("ENG372", "Modern Drama", level300, second_semester),
            ("ENG382", "Contemporary African Fiction", level300, second_semester),

            # 400L FIRST SEMESTER
            ("ENG411", "English Language Studies", level400, first_semester),
            ("ENG421", "Advanced Discourse Analysis", level400, first_semester),
            ("ENG431", "Research Methods in English Studies", level400, first_semester),
            ("ENG441", "Language Planning and Policy", level400, first_semester),
            ("ENG451", "English Language Teaching", level400, first_semester),
            ("ENG461", "Literary Criticism", level400, first_semester),
            ("ENG471", "African Literary Theory", level400, first_semester),
            ("ENG481", "Special Author Studies", level400, first_semester),
            ("ENG491", "Seminar in English Studies", level400, first_semester),

            # 400L SECOND SEMESTER
            ("ENG412", "Advanced Studies in English Grammar", level400, second_semester),
            ("ENG422", "Language and Society in Africa", level400, second_semester),
            ("ENG432", "Project", level400, second_semester),
            ("ENG442", "Translation Studies", level400, second_semester),
            ("ENG452", "Applied English Linguistics", level400, second_semester),
            ("ENG462", "Comparative Literature", level400, second_semester),
            ("ENG472", "Contemporary Literary Theory", level400, second_semester),
            ("ENG482", "Special Topics in English Studies", level400, second_semester),
            ("ENG492", "Long Essay / Research Project", level400, second_semester),
        ]

        for code, title, level, semester in courses:
            Course.objects.get_or_create(
                programme=programme,
                code=code,
                defaults={
                    "title": title,
                    "level": level,
                    "semester": semester,
                    "description": title,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded {len(courses)} English courses."
            )
        )