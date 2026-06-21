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
    help = "Seed B.Sc. Development Studies courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Development Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Development Studies"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("DES111", "Introduction to Development Studies I"),
                ("DES113", "Introduction to Political Economy"),
                ("DES115", "Introduction to Sociology"),
                ("DES117", "Development and Society"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("DES112", "Introduction to Development Studies II"),
                ("DES114", "Development Planning"),
                ("DES116", "Nigerian Economy and Development"),
                ("DES118", "Environment and Sustainable Development"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("DES211", "Theories of Development"),
                ("DES213", "Rural Development"),
                ("DES215", "Community Development"),
                ("DES217", "Population and Development"),
                ("DES219", "Development Administration"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("DES212", "Development Planning and Policy"),
                ("DES214", "Urban Development"),
                ("DES216", "Gender and Development"),
                ("DES218", "International Development"),
                ("DES220", "Project Monitoring and Evaluation"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("DES311", "Development Economics"),
                ("DES313", "Public Policy Analysis"),
                ("DES315", "NGOs and Civil Society"),
                ("DES317", "Participatory Development"),
                ("DES319", "Agricultural and Rural Development"),
                ("DES321", "Human Resource Development"),
            ],

            (300, "Second Semester"): [
                ("DES312", "Development Project Management"),
                ("DES314", "Sustainable Livelihoods"),
                ("DES316", "Globalization and Development"),
                ("DES318", "Research Methods in Development Studies"),
                ("DES320", "Poverty and Development"),
                ("DES399", "SIWES"),
            ],

            (400, "First Semester"): [
                ("DES411", "Advanced Development Theory"),
                ("DES413", "Governance and Development"),
                ("DES415", "Development Communication"),
                ("DES417", "International Organizations and Development"),
                ("DES419", "Development Studies Seminar"),
                ("DES421", "Development Project Design"),
            ],

            (400, "Second Semester"): [
                ("DES412", "Development Strategies in Africa"),
                ("DES414", "Local Government and Development"),
                ("DES416", "Leadership and Development"),
                ("DES418", "Monitoring and Evaluation of Development Projects"),
                ("DES420", "Contemporary Development Issues"),
                ("DES499", "Research Project"),
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
                "B.Sc. Development Studies courses seeded successfully."
            )
        )