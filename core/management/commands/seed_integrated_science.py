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
    help = "Seed B.Sc.(Ed) Integrated Science courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Integrated Science Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Integrated Science"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Practical Biology I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Practical Chemistry I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
                ("SED225", "Nigerian Integrated Science Curriculum"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Practical Biology II"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM192", "Introductory Practical Chemistry II"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
                ("SED226", "Concepts and Nature of Integrated Science"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("BIO201", "Genetics I"),
                ("CHM201", "Organic Chemistry I"),
                ("PHY201", "General Physics III"),
                ("SED231", "Chemistry for Integrated Science"),
                ("SED233", "Environmental Education"),
                ("SED281", "Integrated Science Education Methods I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("BIO202", "Genetics II"),
                ("CHM202", "Organic Chemistry II"),
                ("PHY202", "Electromagnetism and Modern Physics"),
                ("SED232", "Earth and Space Science"),
                ("SED234", "Energy and Matter"),
                ("SED282", "Integrated Science Education Methods II"),
            ],

            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("BIO301", "Field Course I"),
                ("CHM301", "Organic Reaction Mechanisms"),
                ("PHY301", "Classical Mechanics"),
                ("SED321", "Laboratory Organisation and Management"),
                ("SED381", "Integrated Science Curriculum Development"),
            ],

            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("BIO302", "Field Course II"),
                ("CHM302", "Spectroscopy"),
                ("PHY302", "Electromagnetic Theory"),
                ("SED322", "Evaluation in Integrated Science"),
                ("SED382", "Practical Approaches to Integrated Science"),
            ],

            (400, "First Semester"): [
                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("SED411", "Practice in Integration of Science"),
                ("SED413", "Science, Technology and Society"),
                ("BIO413", "Developmental Biology"),
            ],

            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("SED470", "Seminar in Integrated Science"),
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
                "B.Sc.(Ed) Integrated Science courses seeded successfully."
            )
        )