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
    help = "Seed B.Sc. Peace Studies and Conflict Resolution courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Peace Studies and Conflict Resolution"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Peace Studies and Conflict Resolution"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("PCR111", "Introduction to Peace Studies"),
                ("PCR113", "Introduction to Peace Education"),
                ("PCR115", "Introduction to Conflict Resolution Processes I"),

                # Electives
                ("POL111", "Elements of Political Science"),
                ("POL121", "Introduction to African Politics"),
                ("ECO121", "Principles of Economics I"),
                ("CSS111", "Introduction to Sociology"),
                ("FRE101", "Basic French Grammar I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("PCR112", "Democracy and Good Governance"),
                ("PCR114", "Introduction to Conflict Resolution"),
                ("CSS132", "Ethnography and Social Structure of Nigeria"),

                # Electives
                ("POL124", "Organization of Government"),
                ("POL126", "Citizens and the State"),
                ("CSS121", "Introduction to Psychology"),
                ("CSS134", "Geography of Nigeria"),
                ("LAW100", "Introduction to Law"),
                ("FRE102", "Basic French Grammar and Composition II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("PCR211", "Conflict and Peace Studies"),
                ("PCR213", "Theories of Conflict"),
                ("PCR215", "Alternative Dispute Resolution I"),
                ("PCR261", "Culture, Values and Conflicts in War"),
                ("PCR263", "Communication and Conflict"),

                # Electives
                ("POL223", "Foundations of Political Economy"),
                ("FRE111", "Language Laboratory Work / Oral French"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("PCR212", "Peace Education and Development"),
                ("PCR214", "Conflict Resolution Processes II"),
                ("PCR216", "Alternative Dispute Resolution II"),
                ("PCR222", "Human Rights and Conflict"),
                ("PCR224", "Gender and Peace Studies"),

                # Electives
                ("LAW242", "Constitutional Law I"),
                ("POL214", "Introduction to Political Analysis"),
            ],

            (300, "First Semester"): [
                ("GST302", "Entrepreneurship Studies"),
                ("PCR311", "Peacekeeping and Peacebuilding"),
                ("PCR313", "Conflict Analysis"),
                ("PCR315", "Negotiation and Mediation"),
                ("PCR351", "Environment and Conflict"),
                ("PCR361", "Security Studies"),
                ("PCR371", "Early Warning and Early Response Systems"),

                # Electives
                ("INR321", "Foreign Policy Analysis"),
                ("LAW243", "Constitutional Law II"),
            ],

            (300, "Second Semester"): [
                ("PCR312", "Peace Research Methods"),
                ("PCR352", "Sustainable Environmental Development and Peace"),
                ("PCR362", "Urban Violence and Security"),
                ("PCR372", "Introduction to Early Warning Mechanism"),
                ("PCR374", "Practical Exercises in Conflict Simulation"),

                # Electives
                ("INR311", "Introduction to Strategic Studies"),
                ("INR322", "Strategic Studies in the 20th Century"),
                ("LAW244", "Constitutional Law II"),
                ("ECO324", "History of Economic Thought"),
            ],

            (400, "First Semester"): [
                ("PCR415", "The Nature of Global Terrorism"),
                ("PCR417", "International Relations and Security"),
                ("PCR419", "International Politics of the Cold War (1945–1991)"),
                ("PCR421", "International Organisations and Peace Building"),
                ("PCR437", "Gender in War and Peace"),

                # Electives
                ("POL431", "Third World Dependency and Development"),
                ("POL421", "The Military and Politics in Africa"),
                ("PCR433", "War and Peace in Greece and Rome"),
                ("INR441", "Contemporary Strategic Studies"),
                ("LAW321", "Environmental Law I"),
            ],

            (400, "Second Semester"): [
                ("PCR412", "Project"),
                ("PCR422", "Globalisation and Peace"),
                ("PCR424", "Governance, International Law and Fundamental Human Rights"),

                # Electives
                ("INR412", "Foreign Policies of Great Powers"),
                ("POL424", "Political Parties and Pressure Groups"),
                ("LAW322", "Environmental Law II"),
                ("CSS452", "Victims of Crimes and Human Rights Violations"),
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
                "B.Sc. Peace Studies and Conflict Resolution courses seeded successfully."
            )
        )