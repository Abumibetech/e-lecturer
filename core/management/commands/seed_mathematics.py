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
    help = "Seed B.Sc. Mathematics courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mathematics"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Mathematics"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("CIT104", "Introduction to Computer Science"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Biology Practical I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("MTH101", "Elementary Mathematics I"),
                ("MTH103", "Elementary Mathematics III"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("MTH102", "Elementary Mathematics II"),
                ("STT102", "Introductory Statistics"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("MTH201", "Linear Algebra I"),
                ("MTH203", "Mathematical Methods I"),
                ("MTH205", "Differential Equations I"),
                ("MTH207", "Real Analysis I"),
                ("MTH209", "Abstract Algebra I"),
                ("STT201", "Probability Theory I"),

                # Electives
                ("CIT211", "Introduction to Operating Systems"),
                ("PHY201", "General Physics III"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("MTH202", "Linear Algebra II"),
                ("MTH204", "Mathematical Methods II"),
                ("MTH206", "Differential Equations II"),
                ("MTH208", "Real Analysis II"),
                ("MTH210", "Abstract Algebra II"),
                ("STT202", "Statistical Methods"),

                # Electives
                ("CIT213", "Elementary Data Processing"),
                ("PHY202", "General Physics IV"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("MTH301", "Complex Analysis I"),
                ("MTH303", "Numerical Analysis I"),
                ("MTH305", "Topology I"),
                ("MTH307", "Vector and Tensor Analysis"),
                ("MTH309", "Operations Research I"),
                ("STT301", "Mathematical Statistics I"),
                ("MTH391", "Mathematics Practical I"),

                # Electives
                ("CIT237", "Programming and Algorithms"),
                ("MTH311", "Graph Theory"),
                ("MTH313", "Mathematical Modelling"),
            ],

            (300, "Second Semester"): [
                ("MTH302", "Complex Analysis II"),
                ("MTH304", "Numerical Analysis II"),
                ("MTH306", "Topology II"),
                ("MTH308", "Operations Research II"),
                ("STT302", "Mathematical Statistics II"),
                ("MTH392", "Mathematics Practical II"),
                ("MTH399", "SIWES"),

                # Electives
                ("CIT341", "Data Structures"),
                ("MTH312", "Discrete Mathematics"),
                ("MTH314", "Computational Mathematics"),
            ],

            (400, "First Semester"): [
                ("MTH401", "Measure Theory"),
                ("MTH403", "Functional Analysis"),
                ("MTH405", "Mathematical Modelling and Simulation"),
                ("MTH407", "Optimization Theory"),
                ("MTH409", "Research Methodology in Mathematics"),
                ("MTH491", "Research Project I"),

                # Electives
                ("MTH411", "Number Theory"),
                ("MTH413", "Financial Mathematics"),
                ("MTH415", "Mathematical Physics"),
            ],

            (400, "Second Semester"): [
                ("MTH402", "Advanced Real Analysis"),
                ("MTH404", "Integral Equations"),
                ("MTH406", "Dynamical Systems"),
                ("MTH408", "Stochastic Processes"),
                ("MTH492", "Research Project II"),

                # Electives
                ("MTH412", "Coding Theory"),
                ("MTH414", "Actuarial Mathematics"),
                ("MTH416", "Cryptography"),
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
                "B.Sc. Mathematics courses seeded successfully."
            )
        )