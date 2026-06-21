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
    help = "Seed B.Sc.(Ed) Chemistry courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Chemistry Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Chemistry"
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
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("MTH101", "Elementary Mathematics I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM104", "Descriptive Inorganic Chemistry"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("MTH102", "Elementary Mathematics II"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("CHM201", "Organic Chemistry I"),
                ("CHM203", "Physical Chemistry I"),
                ("CHM205", "Inorganic Chemistry II"),
                ("CHM207", "Analytical Chemistry I"),
                ("CHM291", "Practical Chemistry III"),
                ("MTH201", "Mathematical Methods I"),
                ("SED283", "Chemistry Education Methods I"),
            ],

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("CHM202", "Organic Chemistry II"),
                ("CHM204", "Physical Chemistry II"),
                ("CHM206", "Inorganic Chemistry III"),
                ("CHM208", "Analytical Chemistry II"),
                ("CHM292", "Practical Chemistry IV"),
                ("PHY202", "Electromagnetism and Modern Physics"),
                ("SED284", "Chemistry Education Methods II"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("CHM301", "Organic Reaction Mechanisms"),
                ("CHM303", "Physical Chemistry III"),
                ("CHM305", "Transition Metal Chemistry"),
                ("CHM307", "Instrumental Analysis"),
                ("CHM309", "Chemical Thermodynamics"),
                ("CHM391", "Advanced Practical Chemistry I"),
                ("SED381", "Laboratory Techniques in Chemistry Education"),
            ],

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("CHM302", "Spectroscopy"),
                ("CHM304", "Quantum Chemistry"),
                ("CHM306", "Environmental Chemistry"),
                ("CHM308", "Industrial Chemistry"),
                ("CHM392", "Advanced Practical Chemistry II"),
                ("SED382", "Curriculum Development in Chemistry Education"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [
                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("CHM401", "Advanced Organic Chemistry"),
                ("CHM403", "Advanced Physical Chemistry"),
                ("CHM405", "Advanced Inorganic Chemistry"),
                ("CHM407", "Polymer Chemistry"),
                ("CHM409", "Research Seminar"),
                ("SED481", "Science, Technology and Society"),
            ],

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("CHM402", "Natural Products Chemistry"),
                ("CHM404", "Industrial and Environmental Chemistry"),
                ("CHM406", "Biochemistry for Chemists"),
                ("CHM408", "Chemical Kinetics"),
                ("CHM410", "Project in Chemistry Education"),
                ("SED482", "Evaluation in Science Education"),
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
                "B.Sc.(Ed) Chemistry courses seeded successfully."
            )
        )