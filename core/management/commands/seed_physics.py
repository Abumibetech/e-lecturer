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
    help = "Seed B.Sc. Physics courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Physics"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Physics"
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
                ("MTH101", "General Mathematics I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY103", "Geometrical and Wave Optics"),
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
                ("MTH102", "General Mathematics II"),
                ("STT102", "Introductory Statistics"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("MTH281", "Mathematical Methods I"),
                ("PHY201", "Classical Mechanics I"),
                ("PHY203", "Electricity and Magnetism I"),
                ("PHY205", "Thermal Physics I"),
                ("PHY207", "Electronics I"),
                ("PHY291", "Physics Laboratory I"),

                # Electives
                ("CHM211", "Analytical Chemistry"),
                ("CSC201", "Introduction to Programming"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("STT202", "Statistical Methods"),
                ("PHY202", "Classical Mechanics II"),
                ("PHY204", "Electricity and Magnetism II"),
                ("PHY206", "Thermal Physics II"),
                ("PHY208", "Electronics II"),
                ("PHY292", "Physics Laboratory II"),

                # Electives
                ("CHM212", "Organic Chemistry II"),
                ("MTH282", "Mathematical Methods II"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("PHY301", "Mathematical Physics I"),
                ("PHY303", "Quantum Physics I"),
                ("PHY305", "Electrodynamics I"),
                ("PHY307", "Solid State Physics I"),
                ("PHY309", "Computational Physics"),
                ("PHY391", "Physics Laboratory III"),

                # Electives
                ("PHY351", "Atmospheric Physics I"),
                ("PHY361", "Geophysics I"),
                ("PHY371", "Renewable Energy Physics"),
            ],

            (300, "Second Semester"): [
                ("PHY302", "Mathematical Physics II"),
                ("PHY304", "Quantum Physics II"),
                ("PHY306", "Electronics III"),
                ("PHY308", "Atomic and Molecular Physics"),
                ("PHY399", "SIWES"),

                # Electives
                ("PHY352", "Atmospheric Physics II"),
                ("PHY362", "Geophysics II"),
                ("PHY372", "Solar Energy Technology"),
            ],

            (400, "First Semester"): [
                ("PHY401", "Elementary Particle Physics"),
                ("PHY405", "Electronics III"),
                ("PHY407", "Solid State Physics II"),
                ("PHY499", "Project"),

                # Electives
                ("PHY455", "Lower Atmospheric Physics"),
                ("PHY457", "Environmental Physics"),
                ("PHY461", "Geophysics III"),
            ],

            (400, "Second Semester"): [
                ("PHY404", "Electrodynamics II"),
                ("PHY492", "Laboratory Physics III"),

                # Electives
                ("PHY402", "Nuclear Physics"),
                ("PHY406", "Optics III"),
                ("PHY456", "Nuclear Reactor Physics"),
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
                "B.Sc. Physics courses seeded successfully."
            )
        )