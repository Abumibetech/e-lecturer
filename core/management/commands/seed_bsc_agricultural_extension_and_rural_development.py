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
    help = "Seed B.Sc. Agricultural Extension and Rural Development courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Agricultural Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Agricultural Extension and Rural Development"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Agricultural Extension and Rural Development"
        )

        courses = {

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("CIT101", "Computers in Society"),
                ("GST121", "Use of Library"),
                ("GST105", "History and Philosophy of Science"),
                ("BIO101", "General Biology I"),
                ("BIO191", "Practical Biology"),
                ("CHM101", "Introduction to Inorganic Chemistry I"),
                ("CHM191", "Practical Chemistry I"),
                ("AGR101", "Mathematics for Agriculture I"),
                ("PHY121", "General Physics"),
                ("PHY191", "Practical Physics I"),
                ("CHM131", "Organic Chemistry for Agriculture I"),
                ("SLM201", "Principles of Soil Science"),
            ],

            # =========================
            # 100 LEVEL SECOND SEMESTER
            # =========================
            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("BIO102", "General Biology II"),
                ("BIO192", "Practical Biology II"),
                ("CHM102", "Introduction to Inorganic Chemistry II"),
                ("CHM192", "Practical Chemistry II"),
                ("AGR102", "Mathematics for Agriculture II"),
                ("PHY122", "General Physics II"),
                ("PHY192", "Practical Physics II"),
                ("CHM132", "Organic Chemistry for Agriculture II"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("ANP201", "Introduction to Biotechnology"),
                ("FRM211", "Forestry and Wildlife Management"),
                ("AGR203", "Principles of Crop Production"),
                ("AGR205", "Introduction to Agro-Climatology"),
                ("ARD203", "Introduction to Home Economics"),
                ("SLM201", "Principles of Soil Science"),
            ],

            # =========================
            # 200 LEVEL SECOND SEMESTER
            # =========================
            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("ANP202", "Introduction to Animal Production"),
                ("AEC202", "Principles of Agricultural Economics"),
                ("ARD202", "Introduction to Agricultural Extension and Rural Sociology"),
                ("CRP202", "Principles of Crop Protection"),
                ("FST202", "Introduction to Food Science and Technology"),
                ("SLM202", "Land Resources Evaluation"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [
                ("ARD301", "Agricultural Extension Education"),
                ("ARD303", "Comparative Agricultural Extension Systems"),
                ("ARD305", "Rural Sociology"),
                ("ARD307", "Educational Psychology and Extension Methods"),
                ("AEC301", "Farm Management"),
                ("AEC303", "Agricultural Statistics"),
                ("CRP301", "Principles of Crop Protection"),
                ("ANP301", "Animal Husbandry and Production"),

                # Electives
                ("AEC305", "Agribusiness Management"),
                ("ARD309", "Social Action and Group Dynamics"),
                ("ARD311", "Environmental Extension"),
                ("ARD313", "Development Communication"),
            ],

            # =========================
            # 300 LEVEL SECOND SEMESTER
            # =========================
            (300, "Second Semester"): [
                ("ARD302", "Extension Teaching Learning Process and Methods"),
                ("ARD304", "Extension Principles and Organisation"),
                ("ARD306", "Agricultural Journalism"),
                ("ARD308", "Extension Strategies in Rural Development Projects"),
                ("AGM314", "Introduction to Farm Mechanisation"),
                ("APT300", "Agricultural Practical Training"),

                # Electives
                ("AEC314", "Agribusiness Management"),
                ("ARD316", "Environmental Extension"),
                ("ARD317", "Development Communication in Extension"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [
                ("AEC401", "Farm Management Records and Accounts"),
                ("SLM401", "Soil Fertility and Water Management"),
                ("SLM403", "Farm Design, Survey and Land Use Planning"),
                ("CRP401", "Crop Production Practice (Arable and Horticultural Crops)"),
                ("ANP401", "Animal Husbandry Techniques I (Ruminants)"),
                ("ANP403", "Animal Husbandry Techniques II (Non-Ruminants)"),
                ("CRP403", "Crop Protection Techniques"),
                ("CRP405", "Agricultural Processing and Storage"),
            ],

            # =========================
            # 400 LEVEL SECOND SEMESTER
            # =========================
            (400, "Second Semester"): [
                ("ARD401", "Community Agricultural Extension"),
                ("AEC403", "Agricultural Finance"),
                ("AEC405", "Entrepreneurship in Agribusiness"),
                ("AGM401", "Agricultural Mechanisation and Workshop Practice II"),
                ("AGM403", "Agricultural Mechanisation and Workshop Practice III"),
                ("APT400", "Agricultural Industrial Training"),
            ],

            # =========================
            # 500 LEVEL FIRST SEMESTER
            # =========================
            (500, "First Semester"): [
                ("ARD501", "Diffusion and Adoption of Innovations"),
                ("ARD503", "Agricultural Extension Administration and Supervision"),
                ("ARD505", "Programme Planning and Evaluation in Extension"),
                ("ARD507", "Rural Development Planning"),
                ("ARD509", "Research Methods in Agricultural Extension"),

                # Electives
                ("ARD511", "Gender Issues in Agricultural Extension"),
                ("ARD513", "ICT Applications in Agricultural Extension"),
            ],

            # =========================
            # 500 LEVEL SECOND SEMESTER
            # =========================
            (500, "Second Semester"): [
                ("ARD502", "Agricultural Extension Programme Development"),
                ("ARD504", "Leadership Development in Rural Communities"),
                ("ARD506", "Monitoring and Evaluation in Rural Development"),
                ("ARD508", "Seminar in Agricultural Extension and Rural Development"),
                ("ARD590", "Project"),

                # Electives
                ("ARD512", "Contemporary Issues in Rural Development"),
                ("ARD514", "Agricultural Information Systems"),
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
                "B.Sc. Agricultural Extension and Rural Development courses seeded successfully."
            )
        )