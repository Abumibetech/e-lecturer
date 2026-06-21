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
    help = "Seed B.Sc. Biology courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Science"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Biology"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Biology"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("BIO101", "General Biology I"),
                ("BIO191", "General Biology Practical I"),
                ("CHM101", "Introductory Inorganic Chemistry"),
                ("CHM103", "Introductory Physical Chemistry"),
                ("CHM191", "Introductory Chemistry Practical I"),
                ("MTH101", "Elementary Mathematics I"),
                ("PHY101", "Elementary Mechanics, Heat and Properties of Matter"),
                ("PHY191", "Introductory Physics Practical I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("BIO102", "General Biology II"),
                ("BIO192", "General Biology Practical II"),
                ("CHM102", "Introductory Organic Chemistry"),
                ("CHM192", "Introductory Chemistry Practical II"),
                ("MTH102", "Elementary Mathematics II"),
                ("PHY102", "Electricity, Magnetism and Modern Physics"),
                ("PHY192", "Introductory Physics Practical II"),
                ("STT102", "Introductory Statistics"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("BIO201", "Genetics I"),
                ("BIO203", "Cell Biology"),
                ("BIO205", "General Ecology"),
                ("BIO207", "Invertebrate Zoology"),
                ("BIO209", "Plant Morphology and Taxonomy"),
                ("BIO211", "Introductory Biochemistry"),

                # Electives
                ("CHM211", "Analytical Chemistry"),
                ("MTH281", "Mathematical Methods I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("BIO202", "Genetics II"),
                ("BIO204", "Microbiology I"),
                ("BIO206", "Vertebrate Zoology"),
                ("BIO208", "Plant Physiology"),
                ("BIO210", "Evolutionary Biology"),
                ("BIO212", "Introductory Biotechnology"),

                # Electives
                ("CHM212", "Organic Chemistry II"),
                ("STT202", "Statistical Methods"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("BIO301", "Molecular Biology"),
                ("BIO303", "Animal Physiology"),
                ("BIO305", "Plant Ecology"),
                ("BIO307", "Mycology"),
                ("BIO309", "Environmental Biology"),
                ("BIO311", "Biostatistics"),
                ("BIO391", "Biology Practical I"),

                # Electives
                ("BIO313", "Limnology"),
                ("BIO315", "Ethnobotany"),
                ("BIO317", "Conservation Biology"),
            ],

            (300, "Second Semester"): [
                ("BIO302", "Population Genetics"),
                ("BIO304", "Microbiology II"),
                ("BIO306", "Developmental Biology"),
                ("BIO308", "Economic Botany"),
                ("BIO310", "Parasitology"),
                ("BIO312", "Immunology"),
                ("BIO392", "Biology Practical II"),

                # Electives
                ("BIO314", "Marine Biology"),
                ("BIO316", "Applied Entomology"),
                ("BIO318", "Environmental Toxicology"),
            ],

            (400, "First Semester"): [
                ("BIO401", "Cytogenetics"),
                ("BIO403", "Plant Physiology II"),
                ("BIO405", "Advanced Ecology"),
                ("BIO407", "Animal Behaviour"),
                ("BIO409", "Fisheries Biology"),
                ("BIO411", "Wildlife Management and Conservation"),
                ("BIO491", "Research Project I"),

                # Electives
                ("BIO413", "Industrial Microbiology"),
                ("BIO415", "Biotechnology Applications"),
            ],

            (400, "Second Semester"): [
                ("BIO402", "Cytogenetics of Plants"),
                ("BIO404", "Systematic Biology"),
                ("BIO408", "Soil Ecology"),
                ("BIO410", "Fisheries and Aquaculture"),
                ("BIO412", "Wildlife Ecology and Conservation"),
                ("BIO492", "Research Project II"),

                # Electives
                ("BIO406", "Parasitology and Immunology"),
                ("BIO414", "Applied Entomology"),
                ("BIO416", "Industrial Microbiology"),
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
                "B.Sc. Biology courses seeded successfully."
            )
        )