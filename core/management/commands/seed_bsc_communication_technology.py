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
    help = "Seed B.Sc. Communication Technology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Computing"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Communication Technology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Communication Technology"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("BIO101", "General Biology I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CIT101", "Computers in Society"),
                ("CIT143", "Introduction to Data Organisation and Management"),
                ("MTH121", "Linear Algebra I"),
                ("PHY111", "Elementary Mechanics"),
                ("PHY113", "Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("GST105", "History and Philosophy of Science"),
                ("GST122", "Introduction to Philosophy and Logic"),
                ("CIT102", "Software Application Skills"),
                ("CIT132", "Programming in BASIC"),
                ("MTH102", "Introductory Statistics"),
                ("MTH112", "Differential Calculus"),
                ("MTH122", "Integral Calculus"),
                ("MTH142", "Vectors and Geometry"),
                ("PHY132", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
            ],

            (200, "First Semester"): [
                ("CIT211", "Introduction to Operating Systems"),
                ("CIT213", "Elementary Data Processing"),
                ("CIT215", "Introduction to Programming Languages"),
                ("CIT237", "Programming and Algorithms"),
                ("MTH281", "Mathematical Methods I"),
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("MTH213", "Numerical Analysis I"),
                ("MTH231", "Linear Algebra II"),
            ],

            (200, "Second Semester"): [
                ("CIT208", "Information Systems"),
                ("CIT212", "Systems Analysis and Design"),
                ("CIT246", "Computer Organisation"),
                ("CIT292", "Computer Laboratory I"),
                ("MTH232", "Linear Algebra"),
                ("MTH242", "Differential Equations"),
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("CIT224", "Introduction to Web Technology"),
                ("CIT216", "Computer Programming I"),
                ("MTH282", "Mathematical Methods II"),
            ],

            (300, "First Semester"): [
                ("CIT303", "Principles of Communication Technology"),
                ("CIT305", "Networking and Communication Technology"),
                ("CIT309", "Computer Architecture"),
                ("CIT311", "Computer Networks"),
                ("DAM301", "Data Mining and Data Warehousing"),
                ("CIT341", "Data Structures"),
                ("CIT371", "Introduction to Computer Graphics and Animation"),
                ("CIT381", "File Processing and Management"),
            ],

            (300, "Second Semester"): [
                ("CIT342", "Formal Languages and Automata Theory"),
                ("CIT344", "Introduction to Computer Design"),
                ("CIT389", "Industrial Training (SIWES)"),
                ("CIT392", "Computer Laboratory II"),
                ("DAM364", "Management Information Systems"),
                ("CIT322", "Introduction to Internet Programming"),
                ("DAM344", "Semantic Data Modelling"),
                ("DAM382", "Information Systems Management"),
            ],

            (400, "First Semester"): [
                ("CIT403", "Emerging Technologies"),
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
                ("DAM461", "Statistical Database Systems"),
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
                "B.Sc. Communication Technology courses seeded successfully."
            )
        )