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
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("CIT143", "Introduction to Data Organisation and Management"),
                ("GST101", "Use of English & Communication Skills I"),
                ("CIT101", "Computers in Society"),
                ("MTH103", "Elementary Mathematics III"),
                ("MTH101", "Elementary Mathematics I"),
                ("PHY191", "Introductory Practical Physics I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("GST107", "The Good Study Guide"),
            ],

            (100, "Second Semester"): [
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Physics Laboratory II"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("MTH102", "Elementary Mathematics II"),
                ("STT102", "Introductory Statistics"),
                ("CIT102", "Software Application Skills"),
                ("EDU114", "History of Education"),
                ("EDU112", "Professionalism in Teaching"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("GST102", "Use of English & Communication Skills II"),
                ("BIO102", "Elementary Biology II"),
            ],

            (200, "First Semester"): [
                ("MTH281", "Mathematical Methods I"),
                ("MTH213", "Numerical Analysis I"),
                ("CIT213", "Elementary Data Processing"),
                ("CIT211", "Introduction to Operating Systems"),
                ("EDU233", "General Teaching Methods"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("CIT237", "Programming and Algorithms"),
                ("CIT215", "Introduction to Programming Languages"),
            ],

            (200, "Second Semester"): [
                ("CIT292", "Computer Laboratory I"),
                ("CIT246", "Computer Organisation"),
                ("CIT212", "Systems Analysis and Design"),
                ("CIT208", "Information Systems"),
                ("EDU258", "Computer Science Methods"),
                ("EDU214", "Philosophy of Education"),
                ("EDU212", "Sociology of Education"),
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
            ],

            (300, "First Semester"): [
                ("CIT392", "Computer Laboratory II"),
                ("CIT389", "Industrial Training / SIWES"),
                ("CIT381", "File Processing and Management"),
                ("CIT383", "Introduction to Object-Oriented Programming"),
                ("CIT353", "Introduction to Human-Computer Interaction"),
                ("CIT351", "C# Programming"),
                ("CIT311", "Computer Networks"),
                ("CIT309", "Computer Architecture"),
                ("EDU335", "Teaching Practice I"),
                ("EDU323", "Basic Research Methods in Education"),
                ("GST301", "Entrepreneurship Studies"),
                ("CIT371", "Introduction to Computer Graphics and Animations"),
                ("CIT341", "Data Structures"),
                ("CIT333", "Software Engineering I"),
                ("STT211", "Probability Distribution I"),
            ],

            (300, "Second Semester"): [
                ("EDU421", "Guidance and Counselling"),
                ("CIT344", "Introduction to Computer Design"),
                ("CIT342", "Formal Languages and Automata Theory"),
                ("CIT322", "Introduction to Internet Programming"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU321", "Psychology of Learning"),
            ],

            (400, "First Semester"): [
                ("CIT461", "Internet Architecture and Communication"),
                ("CIT445", "Principles and Techniques of Compilers"),
                ("CIT427", "Database Systems and Management"),
                ("CIT425", "Operations Research"),
                ("CIT411", "Microcomputers and Microprocessors"),
                ("CIT403", "Measurement and Evaluation"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("CIT465", "Network Administration"),
                ("CIT467", "Visual Programming and Applications"),
            ],

            (400, "Second Semester"): [
                ("CIT484", "Website Design and Programming"),
                ("CIT474", "Software Engineering II"),
                ("CIT432", "Software Engineering II"),
                ("CIT412", "Modelling and Simulation"),
                ("EDU426", "Special Education"),
                ("EDU420", "Research Project"),
                ("EDU412", "Visual Programming and Applications"),
                ("CIT478", "Artificial Intelligence"),
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
                "B.Sc.(Ed) Computer Science Education courses seeded successfully."
            )
        )