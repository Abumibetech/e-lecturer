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
    help = "Seed B.Sc.(Ed) Mathematics Education courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mathematics Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Mathematics Education"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("EDU111", "Introduction to Foundations of Education"),
                ("MTH101", "Elementary Mathematics I"),
                ("MTH103", "Elementary Mathematics III"),
                ("MTH105", "Elementary Mathematics V"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Practical Physics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education"),
                ("CIT102", "Software Application Skills"),
                ("MTH102", "Elementary Mathematics II"),
                ("MTH104", "Elementary Mathematics IV"),
                ("MTH106", "Elementary Mathematics VI"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Practical Physics II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("MTH201", "Mathematical Methods I"),
                ("MTH203", "Linear Algebra I"),
                ("MTH205", "Real Analysis I"),
                ("MTH207", "Abstract Algebra I"),
                ("MTH281", "Mathematics Education Methods I"),
                ("CIT211", "Computer Programming I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("MTH202", "Mathematical Methods II"),
                ("MTH204", "Linear Algebra II"),
                ("MTH206", "Real Analysis II"),
                ("MTH208", "Abstract Algebra II"),
                ("MTH282", "Mathematics Education Methods II"),
                ("STA202", "Probability Theory I"),
            ],

            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("MTH301", "Differential Equations I"),
                ("MTH303", "Numerical Analysis I"),
                ("MTH305", "Complex Analysis I"),
                ("MTH307", "Vector and Tensor Analysis"),
                ("MTH381", "Curriculum Development in Mathematics Education"),
                ("STA301", "Mathematical Statistics I"),
            ],

            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("MTH302", "Differential Equations II"),
                ("MTH304", "Numerical Analysis II"),
                ("MTH306", "Complex Analysis II"),
                ("MTH308", "Operational Research I"),
                ("MTH382", "Laboratory Techniques in Mathematics Education"),
            ],

            (400, "First Semester"): [
                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("MTH401", "Topology I"),
                ("MTH403", "Mathematical Modelling"),
                ("MTH405", "Advanced Algebra"),
                ("MTH407", "Advanced Real Analysis"),
                ("MTH409", "Research Seminar"),
                ("SED413", "Science, Technology and Society"),
            ],

            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("MTH402", "Topology II"),
                ("MTH404", "Mathematical Logic"),
                ("MTH406", "Functional Analysis"),
                ("MTH408", "Operational Research II"),
                ("MTH410", "Project in Mathematics Education"),
                ("SED482", "Evaluation in Science Education"),
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
                "B.Sc.(Ed) Mathematics Education courses seeded successfully."
            )
        )