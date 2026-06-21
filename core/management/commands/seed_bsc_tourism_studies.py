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
    help = "Seed B.Sc. Tourism Studies courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Management Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Tourism Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Tourism Studies"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("TSM141", "Understanding Tourism"),
                ("TSM143", "Tourism Services and Operations"),
                ("TSM145", "Geography of Tourism"),
                ("TSM147", "Tourism Policy and Planning"),
                ("FMS105", "Elements of Management I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("ECO122", "Principles of Economics II"),
                ("FMS106", "Elements of Management II"),
                ("MKT108", "Introduction to Marketing"),
                ("COP114", "Cooperative Principles"),
                ("TSM142", "Tourism as an Industry"),
                ("TSM144", "Tourism Marketing"),
                ("TSM146", "The Cultural Heritage"),
                ("MAC134", "Principles and Practice of Public Relations"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("TSM221", "Ecotourism"),
                ("TSM241", "Understanding Tourists and Hosts"),
                ("TSM243", "Tourist Sites: Products and Operations I"),
                ("CSS121", "Introduction to Psychology"),
                ("HCM231", "Food and Beverage Operations"),
                ("HCM233", "Front Office Operations"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("TSM222", "Sustainable Tourism Development"),
                ("TSM242", "Tourism Destination Management"),
                ("TSM244", "Tourist Sites: Products and Operations II"),
                ("HCM232", "Accommodation Management"),
                ("HCM234", "Housekeeping Operations"),
                ("MKT201", "Principles of Marketing"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("TSM341", "Tourism Planning and Development"),
                ("TSM343", "Recreation and Leisure Studies"),
                ("TSM345", "Tourism Impact Assessment"),
                ("TSM347", "Tourism Economics"),
                ("HCM331", "Hospitality Accounting"),
                ("HCM333", "Hospitality Human Resource Management"),
            ],

            (300, "Second Semester"): [
                ("FMS304", "Research Methodology"),
                ("TSM342", "Concept, Design and Feasibility I"),
                ("TSM344", "Tourism Project Development"),
                ("TSM346", "International Tourism"),
                ("BHM302", "Business Hospitality Management"),
                ("TSM399", "SIWES"),
            ],

            (400, "First Semester"): [
                ("TSM403", "Cultural Tourism"),
                ("TSM441", "Strategic Management in Hospitality and Tourism"),
                ("TSM447", "Seminar in Tourism Studies"),
                ("HCM435", "Security and Loss Prevention Management"),
                ("HCM439", "Hotel Planning and Interior Design"),
                ("ECO445", "International Trade and Finance I"),
                ("BFN421", "Risk Management and Insurance"),
            ],

            (400, "Second Semester"): [
                ("TSM442", "Tourism Entrepreneurship"),
                ("TSM444", "Global Tourism Issues"),
                ("TSM450", "Research Project"),
                ("HCM432", "Hospitality Information Systems"),
                ("HCM434", "Lodging Facilities Management"),
                ("HCM436", "Internal Control in Hospitality Administration"),
                ("HCM438", "Hospitality Supervision and Quality Management"),
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
                "B.Sc. Tourism Studies courses seeded successfully."
            )
        )