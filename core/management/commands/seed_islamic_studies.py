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
    help = "Seed B.A. Islamic Studies Courses"

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
            name="Islamic Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A. Islamic Studies"
        )

        courses = {

            (100, "First Semester"): [
                ("ISL101", "General Introduction to Islam"),
                ("ISL111", "Studies on the Qur'an"),
                ("ISL113", "Qur'anic Ethics"),
                ("ISL121", "Studies on the Hadith"),
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("ISL102", "Introduction to Islamic Law"),
                ("ISL112", "Introduction to Tafsir"),
                ("ISL122", "Introduction to Sirah"),
                ("ISL124", "Islamic Moral Theology"),
            ],

            (200, "First Semester"): [
                ("ISL211", "Sciences of the Qur'an"),
                ("ISL213", "Hadith Literature"),
                ("ISL221", "Islamic Theology I"),
                ("ISL223", "Islamic Law I"),
                ("ISL231", "Islamic History and Civilization I"),
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
            ],

            (200, "Second Semester"): [
                ("ISL212", "Qur'anic Exegesis"),
                ("ISL214", "Hadith Criticism"),
                ("ISL222", "Islamic Theology II"),
                ("ISL224", "Islamic Law II"),
                ("ISL232", "Islamic History and Civilization II"),
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            ],

            (300, "First Semester"): [
                ("ISL311", "Advanced Qur'anic Studies"),
                ("ISL313", "Advanced Hadith Studies"),
                ("ISL321", "Islamic Philosophy"),
                ("ISL323", "Islamic Jurisprudence"),
                ("ISL331", "Islam and Contemporary Society"),
                ("ISL341", "Comparative Religion"),
                ("GST302", "Entrepreneurship Studies"),
            ],

            (300, "Second Semester"): [
                ("ISL312", "Themes of the Qur'an"),
                ("ISL314", "Hadith and Contemporary Issues"),
                ("ISL322", "Islamic Ethics"),
                ("ISL324", "Islamic Political Thought"),
                ("ISL332", "Islam in Africa"),
                ("ISL342", "Religion and Social Change"),
            ],

            (400, "First Semester"): [
                ("ISL411", "Advanced Tafsir"),
                ("ISL421", "Advanced Islamic Theology"),
                ("ISL431", "Islam and Modern Challenges"),
                ("ISL441", "Islamic Reform Movements"),
                ("ISL471", "Research Methods in Islamic Studies"),
            ],

            (400, "Second Semester"): [
                ("ISL412", "Contemporary Issues in Islam"),
                ("ISL422", "Islam and Interfaith Relations"),
                ("ISL432", "Islam and Globalization"),
                ("ISL472", "Project"),
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
                f"Successfully seeded {total} Islamic Studies courses."
            )
        )