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
    help = "Seed B.Sc. Environmental Management and Toxicology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Environmental Management and Toxicology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Environmental Management and Toxicology"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Biology Practical I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM191", "Introductory Chemistry Practical I"),
                ("PHY111", "Elementary Mechanics"),
                ("PHY113", "Heat and Properties of Matter"),
                ("MTH101", "General Mathematics I"),
                ("ESM102", "The Nigerian Environment"),
                ("ESM104", "Introduction to Environmental Science"),
                ("ESM106", "Environmental Resource Management"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of Library / Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM192", "Introductory Chemistry Practical II"),
                ("MTH102", "General Mathematics II"),
                ("PHY132", "Electricity, Magnetism and Modern Physics"),
                ("ESM112", "Introductory Ecology"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("ESM211", "Global Environmental Issues"),
                ("ESM231", "Introductory Toxicology"),
                ("ESM261", "Geochemistry"),
                ("ESM273", "Earth and Earth Surface Processes"),
                ("ESM291", "Map Analysis"),
                ("ESM234", "Soil Resources"),

                # Electives
                ("ESM206", "Community Participation in Environmental Management"),
                ("ESM212", "Tropical Climatology"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("ESM204", "Environmental Hazards and Disaster Management"),
                ("ESM222", "Water Resource Evaluation"),
                ("ESM236", "Environmental Microbiology"),
                ("ESM238", "Air Photo Interpretation"),
                ("ECO292", "Environmental Economics"),
                ("ESM299", "SIWES I"),

                # Electives
                ("ESM206", "Community Participation in Environmental Management"),
                ("ESM212", "Tropical Climatology"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("ESM301", "Environment, Ecosystems and Man"),
                ("ESM311", "Noise and Air Pollution"),
                ("ESM317", "Land and Water Pollution"),
                ("ESM341", "Instrumentation and Field Methods"),
                ("ESM343", "Climate Change and Environment"),
                ("ESM345", "Applied Climatology"),

                # Electives
                ("PUL303", "Environmental Laws and Policies"),
                ("ESM306", "Environmental Politics"),
            ],

            (300, "Second Semester"): [
                ("CHM314", "Environmental Chemistry"),
                ("ESM304", "Research Methods"),
                ("ESM322", "Water and Waste Water Management"),
                ("ESM328", "Biodiversity Conservation"),
                ("ESM342", "Environmental Impact Assessment and Auditing"),
                ("ESM392", "Remote Sensing"),
                ("ESM399", "SIWES II"),

                # Electives
                ("ESM324", "Urban Environmental Management"),
                ("ESM326", "Oceanography"),
                ("ESM308", "Rural Development Strategies"),
            ],

            (400, "First Semester"): [
                ("ESM401", "Research Project"),
                ("ESM405", "Environmental Protection Agencies"),
                ("ESM407", "Geographic Information System (GIS)"),
                ("ESM423", "Hydrology and Water Resources"),
                ("ESM431", "Environmental Health and Safety"),
            ],

            (400, "Second Semester"): [
                ("ESM403", "Environmental Perception"),
                ("ESM426", "Biogeography"),
                ("ESM428", "Ecology of Natural Resources"),
                ("ESM444", "Industrial Wastes and Water Treatment"),

                # Electives
                ("ESM411", "Population, Environment and Development"),
                ("ESM421", "Elements of Land Surveying"),
                ("ESM422", "Resource Evaluation"),
                ("ESM424", "Fresh Water Ecology"),
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
                "B.Sc. Environmental Management and Toxicology courses seeded successfully."
            )
        )