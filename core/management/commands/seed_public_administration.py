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
    help = "Seed B.Sc. Public Administration courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Public Administration"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Public Administration"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("PAD101", "Introduction to Public Administration"),
                ("ECO101", "Principles of Economics I"),
                ("SOC101", "Introduction to Sociology"),
                ("ACC101", "Introduction to Accounting"),
                ("MTH101", "Elementary Mathematics for Social Sciences"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Communication in English II"),
                ("GST103", "Logic and Philosophy"),
                ("GST201", "Nigerian Peoples and Culture"),
                ("ECO102", "Principles of Economics II"),
                ("POL101", "Introduction to Political Science"),
                ("PSY101", "Introduction to Psychology"),
                ("CIT101", "Computer Fundamentals"),
            ],

            (200, "First Semester"): [
                ("PAD201", "Administrative Theory I"),
                ("POL201", "Elements of Government"),
                ("PAD203", "Public Financial Administration I"),
                ("PAD205", "Human Behaviour in Organizations"),
                ("BUS201", "Principles of Management"),
                ("PAD207", "Research Methods in Social Sciences"),
            ],

            (200, "Second Semester"): [
                ("PAD202", "Administrative Theory II"),
                ("PAD204", "Public Financial Administration II"),
                ("PAD206", "Public Personnel Administration"),
                ("PAD208", "Local Government Administration"),
                ("PAD210", "Nigerian Government and Administration"),
                ("PAD212", "Introduction to Public Policy"),
            ],

            (300, "First Semester"): [
                ("PAD301", "Administrative Law"),
                ("PAD303", "Public Policy Analysis I"),
                ("PAD305", "Inter-Governmental Relations"),
                ("PAD307", "Development Administration"),
                ("PAD309", "E-Governance in Public Sector"),
            ],

            (300, "Second Semester"): [
                ("PAD302", "Public Policy Analysis II"),
                ("PAD304", "Comparative Public Administration"),
                ("PAD306", "Public Sector Economics"),
                ("PAD308", "Structure of Nigerian Government"),

                # Electives
                ("PAD310", "Conflict Management in Public Sector"),
                ("PAD312", "Public Enterprises Management"),
                ("PAD314", "Social Welfare Administration"),
                ("PAD316", "International Public Administration"),
                ("PAD318", "Urban and Regional Administration"),
            ],

            (400, "First Semester"): [
                ("PAD401", "Public Budgeting and Fiscal Policy"),
                ("PAD403", "Strategic Management in Public Sector"),
                ("PAD405", "Public Enterprises and Privatization"),
                ("PAD407", "Planning Theory and Practice"),
                ("PAD409", "Seminar in Public Administration"),
            ],

            (400, "Second Semester"): [
                ("PAD402", "Comparative Local Government Systems"),
                ("PAD404", "Public Personnel Management (Advanced)"),
                ("PAD406", "Governance and Development"),
                ("PAD408", "Research Project / Long Essay"),

                # Electives
                ("PAD410", "International Administration"),
                ("PAD412", "Public Sector Ethics and Accountability"),
                ("PAD414", "Disaster and Risk Management Administration"),
                ("PAD416", "Non-Profit Organization Management"),
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
                "B.Sc. Public Administration courses seeded successfully."
            )
        )