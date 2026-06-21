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
    help = "Seed B.Sc. Political Science courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Political Science"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Political Science"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("POL111", "Elements of Political Science"),
                ("POL121", "Introduction to African Politics"),
                ("POL123", "Nigerian Constitutional Development"),
                ("CSS111", "Introduction to Sociology"),
                ("ECO121", "Principles of Economics I"),

                # Electives
                ("PCR111", "Introduction to Peace Studies"),
                ("PCR113", "Introduction to Peace Education"),
                ("HIS111", "Introduction to Nigerian History"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Communication in English II"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("POL122", "Introduction to Comparative Politics"),
                ("POL124", "Nigerian Government and Politics"),
                ("POL126", "Citizens and the State"),
                ("CSS112", "Introduction to Psychology"),
                ("ECO122", "Principles of Economics II"),

                # Electives
                ("PCR114", "Introduction to Conflict Resolution"),
                ("HIS112", "Africa in World History"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("POL211", "Political Theory I"),
                ("POL213", "Nigerian Political System I"),
                ("POL215", "Public Administration"),
                ("POL217", "Political Behaviour"),
                ("POL219", "Introduction to International Relations"),
                ("POL221", "Local Government Administration"),

                # Electives
                ("SOC201", "Social Statistics"),
                ("ECO211", "Microeconomic Theory I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("POL212", "Political Theory II"),
                ("POL214", "Nigerian Political System II"),
                ("POL216", "Comparative Government and Politics"),
                ("POL218", "Public Policy Analysis"),
                ("POL220", "International Organization"),
                ("POL222", "Research Methods in Political Science"),

                # Electives
                ("SOC202", "Social Research Methods"),
                ("ECO212", "Microeconomic Theory II"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("POL311", "History of Political Thought"),
                ("POL313", "Political Parties and Pressure Groups"),
                ("POL315", "Public Personnel Administration"),
                ("POL317", "International Politics"),
                ("POL319", "Political Sociology"),
                ("POL321", "Nigerian Foreign Policy"),

                # Electives
                ("POL323", "Urban Politics"),
                ("POL325", "Political Leadership"),
            ],

            (300, "Second Semester"): [
                ("POL312", "Contemporary Political Analysis"),
                ("POL314", "Comparative Federalism"),
                ("POL316", "Development Administration"),
                ("POL318", "Political Economy"),
                ("POL320", "African Political Thought"),
                ("POL322", "Political Data Analysis"),
                ("POL324", "Electoral Process and Administration"),

                # Electives
                ("POL326", "Gender and Politics"),
                ("POL328", "Conflict and Security Studies"),
            ],

            (400, "First Semester"): [
                ("POL411", "Civil-Military Relations"),
                ("POL413", "Development Administration"),
                ("POL415", "Third World Dependency and Development"),
                ("POL417", "Public Finance Administration"),
                ("POL419", "Nigerian Foreign Policy"),
                ("POL421", "Peace and Conflict Studies"),

                # Electives
                ("POL423", "Human Rights and Democracy"),
                ("POL425", "Comparative Public Administration"),
            ],

            (400, "Second Semester"): [
                ("POL412", "Politics and Law in Africa"),
                ("POL414", "State and Economy"),
                ("POL416", "Nigerian Local Government"),
                ("POL418", "Political Institutions and Governance"),
                ("POL420", "Research Project"),

                # Electives
                ("POL422", "International Political Economy"),
                ("POL424", "Global Governance"),
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
                "B.Sc. Political Science courses seeded successfully."
            )
        )
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
    help = "Seed B.Sc. Political Science courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Political Science"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Political Science"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("POL111", "Elements of Political Science"),
                ("POL121", "Introduction to African Politics"),
                ("POL123", "Nigerian Constitutional Development"),
                ("CSS111", "Introduction to Sociology"),
                ("ECO121", "Principles of Economics I"),

                # Electives
                ("PCR111", "Introduction to Peace Studies"),
                ("PCR113", "Introduction to Peace Education"),
                ("HIS111", "Introduction to Nigerian History"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Communication in English II"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("POL122", "Introduction to Comparative Politics"),
                ("POL124", "Nigerian Government and Politics"),
                ("POL126", "Citizens and the State"),
                ("CSS112", "Introduction to Psychology"),
                ("ECO122", "Principles of Economics II"),

                # Electives
                ("PCR114", "Introduction to Conflict Resolution"),
                ("HIS112", "Africa in World History"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("POL211", "Political Theory I"),
                ("POL213", "Nigerian Political System I"),
                ("POL215", "Public Administration"),
                ("POL217", "Political Behaviour"),
                ("POL219", "Introduction to International Relations"),
                ("POL221", "Local Government Administration"),

                # Electives
                ("SOC201", "Social Statistics"),
                ("ECO211", "Microeconomic Theory I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("POL212", "Political Theory II"),
                ("POL214", "Nigerian Political System II"),
                ("POL216", "Comparative Government and Politics"),
                ("POL218", "Public Policy Analysis"),
                ("POL220", "International Organization"),
                ("POL222", "Research Methods in Political Science"),

                # Electives
                ("SOC202", "Social Research Methods"),
                ("ECO212", "Microeconomic Theory II"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("POL311", "History of Political Thought"),
                ("POL313", "Political Parties and Pressure Groups"),
                ("POL315", "Public Personnel Administration"),
                ("POL317", "International Politics"),
                ("POL319", "Political Sociology"),
                ("POL321", "Nigerian Foreign Policy"),

                # Electives
                ("POL323", "Urban Politics"),
                ("POL325", "Political Leadership"),
            ],

            (300, "Second Semester"): [
                ("POL312", "Contemporary Political Analysis"),
                ("POL314", "Comparative Federalism"),
                ("POL316", "Development Administration"),
                ("POL318", "Political Economy"),
                ("POL320", "African Political Thought"),
                ("POL322", "Political Data Analysis"),
                ("POL324", "Electoral Process and Administration"),

                # Electives
                ("POL326", "Gender and Politics"),
                ("POL328", "Conflict and Security Studies"),
            ],

            (400, "First Semester"): [
                ("POL411", "Civil-Military Relations"),
                ("POL413", "Development Administration"),
                ("POL415", "Third World Dependency and Development"),
                ("POL417", "Public Finance Administration"),
                ("POL419", "Nigerian Foreign Policy"),
                ("POL421", "Peace and Conflict Studies"),

                # Electives
                ("POL423", "Human Rights and Democracy"),
                ("POL425", "Comparative Public Administration"),
            ],

            (400, "Second Semester"): [
                ("POL412", "Politics and Law in Africa"),
                ("POL414", "State and Economy"),
                ("POL416", "Nigerian Local Government"),
                ("POL418", "Political Institutions and Governance"),
                ("POL420", "Research Project"),

                # Electives
                ("POL422", "International Political Economy"),
                ("POL424", "Global Governance"),
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
                "B.Sc. Political Science courses seeded successfully."
            )
        )