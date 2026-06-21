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
    help = "Seed B.Sc. Mathematics and Computer Science courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mathematics and Computer Science"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Mathematics and Computer Science"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Biology Practical I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("CIT104", "Introduction to Computer Science"),
                ("MTH101", "Elementary Mathematics I"),
                ("MTH103", "Elementary Mathematics III"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CIT102", "Software Application Skills"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("MTH102", "Elementary Mathematics II"),
                ("STT102", "Introductory Statistics"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Physics Laboratory II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("MTH201", "Linear Algebra I"),
                ("MTH203", "Mathematical Methods I"),
                ("MTH205", "Differential Equations I"),
                ("CIT211", "Introduction to Operating Systems"),
                ("CIT213", "Elementary Data Processing"),
                ("CIT215", "Introduction to Programming Languages"),
                ("CIT237", "Programming and Algorithms"),
                ("STT201", "Probability Theory I"),

                # Electives
                ("PHY201", "General Physics III"),
                ("CHM211", "Analytical Chemistry"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("MTH202", "Linear Algebra II"),
                ("MTH204", "Mathematical Methods II"),
                ("MTH206", "Differential Equations II"),
                ("CIT208", "Information Systems"),
                ("CIT212", "Systems Analysis and Design"),
                ("CIT246", "Computer Organisation"),
                ("CIT292", "Computer Laboratory I"),
                ("STT202", "Statistical Methods"),

                # Electives
                ("PHY202", "General Physics IV"),
                ("CHM212", "Organic Chemistry II"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("MTH301", "Complex Analysis I"),
                ("MTH303", "Numerical Analysis I"),
                ("MTH309", "Operations Research I"),
                ("CIT309", "Computer Architecture"),
                ("CIT311", "Computer Networks"),
                ("CIT341", "Data Structures"),
                ("CIT351", "C# Programming"),
                ("CIT381", "File Processing and Management"),

                # Electives
                ("MTH311", "Graph Theory"),
                ("MTH313", "Mathematical Modelling"),
                ("CIT333", "Software Engineering I"),
            ],

            (300, "Second Semester"): [
                ("MTH302", "Complex Analysis II"),
                ("MTH304", "Numerical Analysis II"),
                ("MTH308", "Operations Research II"),
                ("CIT322", "Introduction to Internet Programming"),
                ("CIT342", "Formal Languages and Automata Theory"),
                ("CIT344", "Computer System Design"),
                ("CIT383", "Object-Oriented Programming"),
                ("CIT392", "Computer Laboratory II"),
                ("CIT399", "SIWES / Industrial Training"),

                # Electives
                ("MTH312", "Discrete Mathematics"),
                ("MTH314", "Computational Mathematics"),
                ("CIT362", "Information Technology and Society"),
            ],

            (400, "First Semester"): [
                ("MTH401", "General Topology I"),
                ("MTH411", "Functional Analysis I"),
                ("CIT411", "Microcomputers and Microprocessors"),
                ("CIT427", "Database Systems and Management"),
                ("CIT461", "Internet Architecture and Communication"),
                ("CIT465", "Network Administration"),

                # Electives
                ("CIT415", "Introduction to E-Commerce"),
                ("CIT445", "Principles and Techniques of Compilers"),
            ],

            (400, "Second Semester"): [
                ("MTH402", "General Topology II"),
                ("MTH412", "Functional Analysis II"),
                ("CIT478", "Artificial Intelligence"),
                ("MTH499", "Project"),

                # Electives
                ("CIT474", "Introduction to Expert System"),
                ("CIT432", "Software Engineering II"),
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
                "B.Sc. Mathematics and Computer Science courses seeded successfully."
            )
        )