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
    help = "Seed B.Sc. Chemistry courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Chemistry"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Chemistry"
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
                ("MTH101", "Elementary Mathematics I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
                ("CIT101", "Computers in Society"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("GST105", "History and Philosophy of Science"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM104", "Descriptive Inorganic Chemistry"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("MTH102", "Elementary Mathematics II"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
                ("CIT102", "Software Application Skills"),
                ("STT102", "Introductory Statistics"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("CHM201", "Physical Chemistry I"),
                ("CHM211", "Inorganic Chemistry I"),
                ("CHM221", "Organic Chemistry I"),
                ("CHM231", "Analytical Chemistry I"),
                ("CHM291", "Practical Chemistry III"),
                ("MTH281", "Mathematical Methods I"),

                # Electives
                ("BIO203", "Cell Biology"),
                ("PHY201", "General Physics III"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("CHM202", "Physical Chemistry II"),
                ("CHM212", "Inorganic Chemistry II"),
                ("CHM222", "Organic Chemistry II"),
                ("CHM232", "Analytical Chemistry II"),
                ("CHM292", "Practical Chemistry IV"),
                ("STT202", "Statistical Methods"),

                # Electives
                ("BIO204", "Microbiology I"),
                ("PHY202", "General Physics IV"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("CHM301", "Chemical Thermodynamics"),
                ("CHM311", "Transition Metal Chemistry"),
                ("CHM321", "Reaction Mechanisms and Organic Synthesis"),
                ("CHM331", "Instrumental Methods of Analysis"),
                ("CHM341", "Environmental Chemistry"),
                ("CHM391", "Practical Chemistry V"),

                # Electives
                ("CHM351", "Polymer Chemistry"),
                ("CHM361", "Industrial Chemistry"),
            ],

            (300, "Second Semester"): [
                ("CHM302", "Chemical Kinetics"),
                ("CHM312", "Coordination Chemistry"),
                ("CHM322", "Natural Products Chemistry"),
                ("CHM332", "Spectroscopic Methods"),
                ("CHM342", "Industrial Chemical Processes"),
                ("CHM392", "Practical Chemistry VI"),
                ("CHM399", "SIWES"),

                # Electives
                ("CHM352", "Petrochemical Chemistry"),
                ("CHM362", "Food Chemistry"),
            ],

            (400, "First Semester"): [
                ("CHM401", "Advanced Physical Chemistry"),
                ("CHM411", "Advanced Inorganic Chemistry"),
                ("CHM421", "Advanced Organic Chemistry"),
                ("CHM431", "Advanced Analytical Chemistry"),
                ("CHM441", "Environmental Pollution and Control"),
                ("CHM491", "Research Project I"),

                # Electives
                ("CHM451", "Medicinal Chemistry"),
                ("CHM461", "Industrial Chemical Technology"),
            ],

            (400, "Second Semester"): [
                ("CHM402", "Quantum Chemistry"),
                ("CHM412", "Bioinorganic Chemistry"),
                ("CHM422", "Heterocyclic Chemistry"),
                ("CHM432", "Advanced Instrumental Analysis"),
                ("CHM442", "Industrial and Environmental Toxicology"),
                ("CHM492", "Research Project II"),

                # Electives
                ("CHM452", "Organometallic Chemistry"),
                ("CHM462", "Materials Chemistry"),
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
                "B.Sc. Chemistry courses seeded successfully."
            )
        )