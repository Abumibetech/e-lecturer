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
    help = "Seed B.Sc.(Ed) Computer Science Education courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Computer Science Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Computer Science Education"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("CIT143", "Introduction to Data Organisation and Management"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("MTH101", "Elementary Mathematics I"),
                ("MTH103", "Elementary Mathematics III"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("CIT102", "Software Application Skills"),
                ("CIT104", "Introduction to Computer Science"),
                ("CIT106", "Introduction to Problem Solving"),
                ("MTH102", "Elementary Mathematics II"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
                ("CHM102", "Introductory Organic Chemistry"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("CIT211", "Computer Programming I"),
                ("CIT215", "Introduction to Computer Systems"),
                ("CIT237", "Object-Oriented Programming"),
                ("CIT255", "Data Structures"),
                ("MTH201", "Mathematical Methods I"),
                ("SED285", "Computer Science Education Methods I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("CIT212", "Computer Programming II"),
                ("CIT216", "Computer Architecture"),
                ("CIT236", "Introduction to Algorithms"),
                ("CIT262", "Systems Analysis and Design"),
                ("CIT264", "Discrete Mathematical Structures"),
                ("SED286", "Computer Science Education Methods II"),
            ],

            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("CIT305", "Operating Systems I"),
                ("CIT313", "Computer Graphics"),
                ("CIT353", "Introduction to Human Computer Interaction"),
                ("CIT371", "Numerical Computation I"),
                ("CIT381", "Introduction to Artificial Intelligence"),
                ("CIT383", "Computer Application Development"),
                ("SED385", "Laboratory Techniques in Computer Science Education"),
            ],

            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU321", "Psychology of Learning"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("CIT306", "Operating Systems II"),
                ("CIT342", "Data Communication"),
                ("CIT344", "Computer Networks"),
                ("CIT392", "Student Industrial Work Experience Scheme"),
                ("SED386", "Curriculum Development in Computer Science Education"),
            ],

            (400, "First Semester"): [
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("CIT403", "Measurement and Evaluation in Computer Science Education"),
                ("CIT411", "Microcomputers and Microprocessors"),
                ("CIT425", "Operations Research"),
                ("CIT427", "Database Systems and Management"),
                ("CIT445", "Principles and Techniques of Compilers"),
                ("CIT461", "Internet Architecture and Communication"),
                ("CIT465", "Network Administration"),
                ("CIT467", "Visual Programming and Applications"),
            ],

            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("CIT412", "Modelling and Simulation"),
                ("CIT432", "Software Engineering II"),
                ("CIT474", "Software Engineering II"),
                ("CIT478", "Artificial Intelligence"),
                ("CIT484", "Website Design and Programming"),
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
                "B.Sc.(Ed) Computer Science Education courses seeded successfully."
            )
        )