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
    help = "Seed B.Sc. Information Technology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Computing"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Information Technology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Information Technology"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST103", "Computer Fundamentals"),
                ("GST107", "The Study Guide for the Distance Learner"),
                ("BIO101", "General Biology I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CIT143", "Introduction to Data Organisation and Management"),
                ("MTH101", "Elementary Mathematics I"),
                ("MTH103", "Elementary Mathematics III"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("BIO191", "General Practical Biology I"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("GST104", "Use of Library"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("CIT104", "Introduction to Computer Science"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("MTH102", "Elementary Mathematics II"),
                ("STT102", "Introductory Statistics"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("PHY192", "Introductory Practical Physics II"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Practical Biology II"),
            ],

            (200, "First Semester"): [
                ("CIT211", "Introduction to Operating Systems"),
                ("CIT213", "Elementary Data Processing"),
                ("CIT215", "Introduction to Programming Languages"),
                ("CIT237", "Programming and Algorithms"),
                ("MTH281", "Mathematical Methods I"),
                ("MTH213", "Numerical Analysis I"),
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
            ],

            (200, "Second Semester"): [
                ("CIT208", "Information Systems"),
                ("CIT212", "Systems Analysis and Design"),
                ("CIT246", "Computer Organisation"),
                ("CIT292", "Computer Laboratory I"),
                ("MTH232", "Linear Algebra I"),
                ("MTH242", "Differential Equations I"),
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("CIT224", "Introduction to Web Technology"),
                ("CIT216", "Computer Programming I"),
            ],

            (300, "First Semester"): [
                ("CIT309", "Computer Architecture"),
                ("CIT311", "Computer Networks"),
                ("CIT341", "Data Structures"),
                ("CIT351", "C# Programming"),
                ("CIT381", "File Processing and Management"),
                ("CIT389", "Industrial Training (SIWES)"),
                ("CIT392", "Computer Laboratory II"),
                ("GST301", "Entrepreneurship Studies"),
                ("CIT333", "Software Engineering I"),
                ("CIT353", "Human Computer Interaction"),
                ("CIT371", "Introduction to Computer Graphics and Animation"),
            ],

            (300, "Second Semester"): [
                ("CIT322", "Introduction to Internet Programming"),
                ("CIT342", "Formal Languages and Automata Theory"),
                ("CIT344", "Computer System Design"),
                ("CIT383", "Object-Oriented Programming"),
                ("CIT387", "Management Information Systems"),
                ("CIT362", "Information Technology and Society"),
                ("CIT364", "Information Security"),
                ("CIT366", "Data Communication"),
            ],

            (400, "First Semester"): [
                ("CIT403", "Seminar on Emerging Technologies"),
                ("CIT411", "Microcomputers and Microprocessors"),
                ("CIT427", "Database Systems and Management"),
                ("CIT461", "Internet Architecture and Communication"),
                ("CIT465", "Network Administration"),
                ("CIT415", "Introduction to E-Commerce"),
                ("CIT445", "Principles and Techniques of Compilers"),
                ("CIT463", "Introduction to Multimedia Technology"),
            ],

            (400, "Second Semester"): [
                ("CIT425", "Operations Research"),
                ("CIT474", "Introduction to Expert Systems"),
                ("DAM461", "Statistical Database System"),
                ("CIT499", "Project"),
                ("CIT478", "Artificial Intelligence"),
                ("CIT484", "Website Design and Programming"),
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
                "B.Sc. Information Technology courses seeded successfully."
            )
        )