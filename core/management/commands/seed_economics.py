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
    help = "Seed B.Sc. Economics courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Economics"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Economics"
        )

        courses = {

            (100, "First Semester"): [
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("FMS105", "Elements of Management I"),
                ("ECO121", "Principles of Economics I"),
                ("ECO153", "Introduction to Quantitative Methods"),

                # Electives
                ("ENT101", "Introduction to Entrepreneurship"),
                ("PCR111", "Introduction to Peace Studies"),
                ("PCR113", "Introduction to Peace Education"),
                ("POL111", "Elements of Political Science"),
                ("CSS111", "Introduction to Sociology"),
                ("CRD124", "Introduction to Cooperatives"),
                ("ENT121", "Principles and Practice of Insurance"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Communication in English II"),
                ("GST105", "History and Philosophy of Science"),
                ("CIT102", "Software Application Skills"),
                ("ECO122", "Principles of Economics II"),
                ("ECO124", "Nigerian Economic History"),
                ("ECO182", "Mathematics for Economists"),
                ("FMS106", "Elements of Management II"),

                # Electives
                ("ACC102", "Principles of Accounting II"),
                ("CSS112", "Introduction to Psychology"),
                ("POL112", "Nigerian Constitutional Development"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("ECO211", "Microeconomic Theory I"),
                ("ECO213", "Macroeconomic Theory I"),
                ("ECO215", "Mathematics for Economists I"),
                ("ECO217", "Statistics for Economists I"),
                ("ECO219", "Structure of the Nigerian Economy"),
                ("ACC201", "Financial Accounting I"),

                # Electives
                ("BUS211", "Principles of Marketing"),
                ("POL221", "Introduction to Public Administration"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("ECO212", "Microeconomic Theory II"),
                ("ECO214", "Macroeconomic Theory II"),
                ("ECO216", "Mathematics for Economists II"),
                ("ECO218", "Statistics for Economists II"),
                ("ECO222", "Public Finance"),
                ("ACC202", "Financial Accounting II"),

                # Electives
                ("BUS212", "Business Communication"),
                ("POL222", "Nigerian Government and Politics"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("ECO311", "Intermediate Microeconomics"),
                ("ECO313", "Intermediate Macroeconomics"),
                ("ECO315", "Econometrics I"),
                ("ECO317", "International Economics I"),
                ("ECO321", "Development Economics I"),
                ("ECO323", "Monetary Economics I"),

                # Electives
                ("ECO325", "Agricultural Economics"),
                ("ECO327", "Labour Economics"),
            ],

            (300, "Second Semester"): [
                ("ECO312", "Intermediate Microeconomics II"),
                ("ECO314", "Intermediate Macroeconomics II"),
                ("ECO316", "Econometrics II"),
                ("ECO318", "International Economics II"),
                ("ECO322", "Development Economics II"),
                ("ECO324", "Monetary Economics II"),
                ("ECO399", "SIWES"),

                # Electives
                ("ECO326", "Industrial Economics"),
                ("ECO328", "Environmental Economics"),
            ],

            (400, "First Semester"): [
                ("ECO411", "Advanced Microeconomic Theory"),
                ("ECO413", "Economics of Production"),
                ("ECO415", "Economic Policy Analysis"),
                ("ECO417", "Comparative Economic Systems"),
                ("ECO419", "Applied Statistics"),
                ("ECO421", "Research Methodology"),

                # Electives
                ("ECO423", "Urban and Regional Economics"),
                ("ECO425", "Problems and Policies of Development"),
                ("ECO427", "Energy Economics"),
            ],

            (400, "Second Semester"): [
                ("ECO412", "Advanced Macroeconomic Theory"),
                ("ECO414", "Taxation and Fiscal Policy"),
                ("ECO416", "Operations Research"),
                ("ECO420", "Project / Long Essay"),
                ("ECO422", "Nigerian Public Finance"),

                # Electives
                ("ACC314", "Management Accounting"),
                ("MGT402", "Management Information System"),
                ("ECO424", "International Finance"),
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
                "B.Sc. Economics courses seeded successfully."
            )
        )