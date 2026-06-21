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
    help = "Seed B.Sc.(Ed) Agricultural Science courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Agricultural Science Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Agricultural Science"
        )

        courses = {

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Practical Biology I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
            ],

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CHM192", "Introductory Practical Chemistry II"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Cultures"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("AGR201", "General Agriculture"),
                ("AEM201", "Principles of Agricultural Extension"),
                ("AGR202", "Introductory Agricultural Engineering"),
                ("AGR203", "Principles of Crop Production"),
                ("BIO201", "Genetics I"),
                ("SOS201", "Principles of Soil Science"),
            ],

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("EDU280", "Agricultural Science Methods"),
                ("AEM212", "Farm Practice"),
                ("ANP202", "Principles of Animal Production"),
                ("BIO220", "Fisheries and Wildlife"),
                ("CHM203", "Organic Chemistry II"),
                ("AFS202", "Agricultural Field Studies"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("ACP303", "Permanent Crops Production"),
                ("ACP305", "Principles of Crop Protection"),
                ("AEM302", "Extension Teaching, Learning Process and Methods"),
                ("ANP301", "Introduction to Non-Ruminant Animal Production"),
                ("ANP313", "Poultry Production"),
                ("SOS301", "Introduction to Pedology and Soil Classification"),
            ],

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("SED305", "Practicum in Science Teaching"),
                ("AEC306", "Farm Records and Accounting"),
                ("AEC308", "Principles of Farm Management"),
                ("AGM314", "Introduction to Farm Mechanisation"),
                ("ANP302", "Ruminant Animal Production"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [
                ("EDU400", "SIWES"),
                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("AEM303", "Agrarian Institutions and Their Management"),
                ("AEM451", "Farm Business Organisation"),
            ],

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("AEC403", "Agricultural Production Economics and Resources"),
                ("AEM405", "Extension, Training and Curriculum Development"),
            ],
        }

        for (level_number, semester_name), course_list in courses.items():

            level, _ = Level.objects.get_or_create(
                name=str(level_number)
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
                "B.Sc.(Ed) Agricultural Science courses seeded successfully."
            )
        )