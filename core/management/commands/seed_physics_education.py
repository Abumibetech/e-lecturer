from django.core.management.base import BaseCommand
from django.utils.text import slugify

from core.models import (
    Faculty,
    Department,
    Programme,
    Level,
    Semester,
    Course,
)


class Command(BaseCommand):
    help = "Seed B.Sc.(Ed) Physics courses (100L - 400L)"

    def handle(self, *args, **kwargs):

        # =========================
        # LEVELS
        # =========================
        levels = {}

        for level in [100, 200, 300, 400]:
            levels[level], _ = Level.objects.get_or_create(
                name=level
            )

        # =========================
        # SEMESTERS
        # =========================
        sem1, _ = Semester.objects.get_or_create(
            name="First Semester"
        )

        sem2, _ = Semester.objects.get_or_create(
            name="Second Semester"
        )

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            slug=slugify("Faculty of Education"),
            defaults={
                "name": "Faculty of Education"
            }
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            slug=slugify("Department of Science Education"),
            defaults={
                "name": "Department of Science Education",
                "faculty": faculty,
            }
        )

        if department.faculty != faculty:
            department.faculty = faculty
            department.save()

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Physics"
        )

        # =========================
        # COURSE DATA
        # =========================
        data = {

            100: {
                sem1: [
                    ("GST101", "Use of English and Communication Skills I"),
                    ("GST105", "History and Philosophy of Science"),
                    ("GST107", "The Good Study Guide"),
                    ("CIT101", "Computers in Society"),
                    ("EDU111", "Introduction to Foundations of Education"),
                    ("MTH101", "Elementary Mathematics I"),
                    ("MTH103", "Elementary Mathematics III"),
                    ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                    ("PHY107", "General Physics Laboratory I"),
                    ("CHM101", "Introductory Inorganic Chemistry"),
                    ("CHM103", "Introductory Physical Chemistry"),
                ],

                sem2: [
                    ("GST102", "Use of English and Communication Skills II"),
                    ("EDU112", "Professionalism in Teaching"),
                    ("EDU114", "History of Education"),
                    ("MTH102", "Elementary Mathematics II"),
                    ("MTH104", "Elementary Mathematics IV"),
                    ("PHY102", "Electricity, Magnetism and Modern Physics"),
                    ("PHY108", "General Physics Laboratory II"),
                    ("CHM102", "Introductory Organic Chemistry"),
                    ("CIT102", "Software Application Skills"),
                ]
            },

            200: {
                sem1: [
                    ("GST201", "Nigerian Peoples and Culture"),
                    ("GST203", "Introduction to Philosophy and Logic"),
                    ("EDU231", "Curriculum Theory and Practice"),
                    ("EDU233", "General Teaching Methods"),
                    ("PHY201", "General Physics III"),
                    ("PHY203", "Mechanics I"),
                    ("PHY205", "Waves and Optics I"),
                    ("PHY207", "Thermal Physics I"),
                    ("MTH201", "Mathematical Methods I"),
                    ("SED287", "Physics Education Methods I"),
                ],

                sem2: [
                    ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                    ("EDU212", "Sociology of Education"),
                    ("EDU214", "Philosophy of Education"),
                    ("PHY202", "Electromagnetism and Modern Physics"),
                    ("PHY204", "Mechanics II"),
                    ("PHY206", "Waves and Optics II"),
                    ("PHY208", "Thermal Physics II"),
                    ("MTH202", "Mathematical Methods II"),
                    ("SED288", "Physics Education Methods II"),
                ]
            },

            300: {
                sem1: [
                    ("GST301", "Entrepreneurship Studies"),
                    ("EDU321", "Psychology of Learning"),
                    ("EDU323", "Basic Research Methods in Education"),
                    ("EDU335", "Teaching Practice I"),
                    ("PHY301", "Classical Mechanics"),
                    ("PHY303", "Electromagnetic Theory I"),
                    ("PHY305", "Quantum Physics I"),
                    ("PHY307", "Electronics I"),
                    ("PHY309", "Mathematical Physics I"),
                    ("SED381", "Laboratory Techniques in Physics Education"),
                ],

                sem2: [
                    ("EDU300", "SIWES"),
                    ("EDU314", "Comparative Education"),
                    ("EDU332", "Educational Technology"),
                    ("EDU336", "Teaching Practice Evaluation and Feedback"),
                    ("PHY302", "Modern Physics"),
                    ("PHY304", "Electromagnetic Theory II"),
                    ("PHY306", "Quantum Physics II"),
                    ("PHY308", "Electronics II"),
                    ("PHY310", "Mathematical Physics II"),
                    ("SED382", "Curriculum Development in Physics Education"),
                ]
            },

            400: {
                sem1: [
                    ("EDU421", "Guidance and Counselling"),
                    ("EDU423", "Measurement and Evaluation"),
                    ("EDU435", "Teaching Practice II"),
                    ("PHY401", "Solid State Physics"),
                    ("PHY403", "Nuclear and Particle Physics"),
                    ("PHY405", "Statistical Mechanics"),
                    ("PHY407", "Geophysics"),
                    ("PHY409", "Research Seminar"),
                    ("SED413", "Science, Technology and Society"),
                ],

                sem2: [
                    ("EDU412", "Principles of Educational Management"),
                    ("EDU420", "Research Project"),
                    ("EDU426", "Special Education"),
                    ("PHY402", "Astrophysics and Cosmology"),
                    ("PHY404", "Advanced Electronics"),
                    ("PHY406", "Computational Physics"),
                    ("PHY408", "Renewable Energy Physics"),
                    ("PHY410", "Project in Physics Education"),
                    ("SED482", "Evaluation in Science Education"),
                ]
            }
        }

        # =========================
        # CREATE COURSES
        # =========================
        created = 0

        for level_number, semesters in data.items():

            level = levels[level_number]

            for semester, courses in semesters.items():

                for code, title in courses:

                    _, was_created = Course.objects.get_or_create(
                        programme=programme,
                        level=level,
                        semester=semester,
                        code=code,
                        defaults={
                            "title": title
                        }
                    )

                    if was_created:
                        created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"SUCCESS: {created} Physics Education courses seeded."
            )
        )