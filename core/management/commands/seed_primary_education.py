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
    help = "Seed Primary Education courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Primary Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Ed. Primary Education"
        )

        courses = {

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
            (100, "First Semester"): [

                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computer in Society"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("EDU113", "Introduction to Educational Psychology"),
                ("PED111", "Introduction to Primary Education"),
                ("PED121", "Child Growth and Development"),
                ("PED122", "Primary English Curriculum and Methods"),
                ("PED144", "Primary Mathematics Curriculum and Methods"),
                ("ENG151", "Introduction to English as a Second Language"),
                ("HCM133", "Agriculture, Nutrition and Health"),
            ],

            # ==========================
            # 100 LEVEL SECOND SEMESTER
            # ==========================
            (100, "Second Semester"): [

                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Application Software Skills"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("PED112", "Reading in Early Childhood and Primary Education"),
                ("PED124", "Social Studies in Primary Education"),
                ("PED126", "Science and Technology in Primary Education"),
                ("STT102", "Introductory Statistics"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [

                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("PED221", "Language Arts in Primary Education"),
                ("PED223", "Mathematics in Primary Education"),
                ("PED225", "Social Studies Curriculum and Methods"),
                ("PED227", "Science Curriculum and Methods"),
                ("PED229", "Classroom Management in Primary Schools"),
            ],

            # ==========================
            # 200 LEVEL SECOND SEMESTER
            # ==========================
            (200, "Second Semester"): [

                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("PED232", "Aesthetic Expression in Primary Education"),
                ("PED234", "Man, Energy and Resources"),
                ("PED236", "Elementary Mechanics"),
                ("PED238", "Assessment and Evaluation in Primary Education"),
                ("PED240", "Guidance Services in Primary Schools"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [

                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("PED313", "Historical and Cultural Background of Immediate Environment"),
                ("PED315", "Integrated Science Teaching Methods"),
                ("PED317", "Language Development and Literacy"),
                ("PED319", "Mathematics Teaching Strategies"),
                ("PED351", "Adult Basic Education"),
            ],

            # ==========================
            # 300 LEVEL SECOND SEMESTER
            # ==========================
            (300, "Second Semester"): [

                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("PED322", "Methods of Teaching Reading in Primary School"),
                ("PED324", "Instructional Materials Development"),
                ("PED326", "Educational Measurement in Primary Education"),
                ("PED328", "Inclusive Education in Primary Schools"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [

                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("PED421", "Developmental Guidance in Primary Education"),
                ("PED423", "Curriculum Development in Primary Education"),
                ("PED425", "School Administration and Supervision"),
                ("PED431", "Continuous Assessment in Primary Education"),
                ("PED433", "Children's Literature"),
            ],

            # ==========================
            # 400 LEVEL SECOND SEMESTER
            # ==========================
            (400, "Second Semester"): [

                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("PED420", "Social Psychology of Instruction"),
                ("PED430", "Design and Production of Learning Materials for Primary School"),
                ("PED432", "Contemporary Issues in Primary Education"),
                ("PED434", "Seminar in Primary Education"),
                ("PED436", "Educational Innovation and Change"),
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
                "Primary Education courses seeded successfully."
            )
        )