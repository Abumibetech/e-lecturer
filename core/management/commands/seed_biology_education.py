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
    help = "Seed B.Sc.(Ed) Biology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Education"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Biology Education"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc.(Ed) Biology"
        )

        courses = {

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
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
            ],

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
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
                ("MTH102", "Elementary Mathematics II"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("EDU231", "Curriculum Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("BIO201", "Genetics I"),
                ("BIO203", "Cell Biology"),
                ("BIO205", "General Physiology I"),
                ("BIO207", "Introductory Ecology"),
                ("CHM201", "Organic Chemistry I"),
                ("SED281", "Biology Education Methods I"),
            ],

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("BIO202", "Genetics II"),
                ("BIO204", "General Physiology II"),
                ("BIO206", "General Ecology"),
                ("BIO208", "Introductory Microbiology"),
                ("CHM202", "Organic Chemistry II"),
                ("SED282", "Biology Education Methods II"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("BIO301", "Field Course I"),
                ("BIO303", "Plant Physiology"),
                ("BIO305", "Animal Physiology"),
                ("BIO307", "Taxonomy of Plants"),
                ("BIO309", "Taxonomy of Animals"),
                ("BIO311", "Evolutionary Biology"),
            ],

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, "Second Semester"): [
                ("EDU300", "SIWES"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Educational Technology"),
                ("EDU336", "Teaching Practice Evaluation and Feedback"),
                ("BIO302", "Field Course II"),
                ("BIO304", "General Ecology"),
                ("BIO306", "General Physiology II"),
                ("BIO308", "Biogeography"),
                ("BIO310", "Protozoology"),
                ("BIO312", "SIWES (Biology)"),
                ("BIO314", "Animal Behaviour"),
                ("BIO316", "Introduction to Bioinformatics"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [
                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("SED413", "Science, Technology and Society"),
                ("BIO401", "Field Course III"),
                ("BIO403", "Population Genetics"),
                ("BIO405", "Hydrobiology"),
                ("BIO407", "Basic Entomology"),
                ("BIO409", "Research Seminar"),
                ("BIO411", "Parasitology"),
            ],

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, "Second Semester"): [
                ("EDU412", "Principles of Educational Management"),
                ("EDU420", "Research Project"),
                ("EDU426", "Special Education"),
                ("BIO402", "Cytogenetics of Plants"),
                ("BIO404", "Systematic Biology"),
                ("BIO408", "Soil Ecology"),
                ("BIO410", "Fisheries and Aquaculture"),
                ("BIO412", "Wildlife Ecology and Conservation"),
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
                "B.Sc.(Ed) Biology courses seeded successfully."
            )
        )