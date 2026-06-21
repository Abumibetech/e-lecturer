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
    help = "Seed Early Childhood Education courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Early Childhood Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Early Childhood Education"
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
                ("ECE113", "Introduction to Philosophy of Early Childhood Education"),
                ("ECE121", "Child Development"),
                ("ECE123", "Health Care in the Early Years"),
                ("PED122", "Primary English Curriculum and Methods"),
                ("PED144", "Primary Mathematics Curriculum Methods"),
                ("ENG151", "Introduction to English as a Second Language"),
                ("HCM133", "Agriculture, Nutrition and Health"),
                ("COP113", "Introduction to General Agriculture I"),
            ],

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
            (100, "Second Semester"): [

                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("ECE110", "Childhood Education in Traditional African Society"),
                ("ECE112", "Origin and Development of Early Childhood Education"),
                ("PED112", "Reading in Early Childhood and Primary Education"),
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
                ("ECE221", "Language and Literacy in the Early Years"),
                ("ECE223", "Play and Learning"),
                ("ECE225", "Meeting Special Needs in Early Childhood Education"),
                ("ECE227", "Organization and Service Provision in Early Childhood Education"),
                ("ECE231", "Science in the Early Years"),
            ],

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, "Second Semester"): [

                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("EDU290", "Early Childhood Education Methods"),
                ("ECE230", "Introduction to Early Childhood Education Curriculum Development"),
                ("ECE232", "Observation, Recording and Assessment in Early Childhood Education"),
                ("PED236", "Elementary Mechanics"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [

                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("ECE313", "Theories and Practice of Early Childhood Education"),
                ("PED237", "Measurement and Shapes"),
                ("PED271", "Primary School Physical and Health Education Curriculum and Methods"),
                ("PED313", "Historical and Cultural Background of Immediate Environment"),
                ("PED351", "Adult Basic Education"),
                ("ENT323", "Entrepreneurship"),
            ],

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, "Second Semester"): [

                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("PED234", "Man, Energy and Resources"),
                ("PED322", "Methods of Teaching Reading in Primary School"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [

                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("ECE413", "Comparative Early Childhood Education"),
                ("ECE421", "Health and Family Life Education"),
                ("PED421", "Developmental Guidance in Primary Education"),
                ("PED431", "Continuous Assessment in Primary Education"),
                ("PED433", "Children Literature"),
            ],

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, "Second Semester"): [

                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("ECE410", "Issues in Early Childhood and Primary Education"),
                ("ECE412", "Management of Early Childhood Education"),
                ("ECE420", "Seminar in Early Childhood Education"),
                ("ECE422", "The School Environment and the Child"),
                ("PED420", "Social Psychology of Instruction"),
                ("PED430", "Design and Production of Learning Materials for Primary School"),
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
                "Early Childhood Education courses seeded successfully."
            )
        )