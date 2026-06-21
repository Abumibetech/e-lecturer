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
    help = "Seed B.Sc. International and Diplomatic Studies courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="International and Diplomatic Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. International and Diplomatic Studies"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("INR111", "Introduction to International Studies"),
                ("INR121", "Structure of the International System"),
                ("ECO121", "Principles of Economics I"),
                ("FRE101", "Basic French Grammar I"),
                ("POL121", "Introduction to African Politics"),

                # Electives
                ("POL111", "Elements of Political Science"),
                ("PCR115", "Introduction to Conflict Resolution Processes I"),
                ("FMS105", "Elements of Management I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("INR112", "Introduction to Law and Diplomacy in Pre-Colonial Africa"),
                ("INR122", "Concepts in International Relations"),
                ("INR132", "Africa and the Western Powers"),
                ("INR162", "International Migration I"),
                ("ECO122", "Principles of Economics II"),
                ("FRE122", "French Grammar II"),

                # Electives
                ("PCR114", "Introduction to Conflict Resolution"),
                ("INR142", "Introduction to Public Administration"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Cultures"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("INR211", "International Law and Diplomacy in the 19th Century"),
                ("INR221", "History and Practice of Diplomacy"),
                ("INR251", "Evolution of Modern International System"),
                ("POL215", "History of Political Thought I"),
                ("POL231", "Essentials of International Relations and Diplomacy"),
                ("FRE221", "French Grammar and Composition I"),

                # Electives
                ("INR231", "South-South Cooperation"),
                ("POL221", "Nigerian Government and Politics I"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("INR212", "International Law and Diplomacy in the 20th Century"),
                ("INR232", "Introduction to Foreign Policy"),
                ("INR242", "Pre-Colonial African Diplomacy"),
                ("INR262", "International Migration II"),
                ("POL212", "Basic Statistics for Social Sciences"),
                ("FRE222", "French Grammar and Composition II"),

                # Electives
                ("INR222", "Europe from French Revolution to the World Wars"),
                ("POL214", "Introduction to Political Analysis"),
            ],

            (300, "First Semester"): [
                ("GST301", "Entrepreneurship Studies"),
                ("INR321", "Foreign Policy Analysis"),
                ("INR331", "International Law"),
                ("INR361", "Religion, Ethnicity and Nationalism in International Politics"),
                ("INR381", "International Negotiations and Diplomacy"),
                ("INR391", "Nigeria's Foreign Policy I"),
                ("POL311", "Contemporary Political Analysis"),

                # Electives
                ("INR341", "Asia in World Politics"),
                ("INR351", "Europe in World Politics"),
                ("INR371", "BRICS and Multilateral Diplomacy"),
            ],

            (300, "Second Semester"): [
                ("INR300", "Theories in International Relations"),
                ("INR312", "American Diplomacy in the 20th Century"),
                ("INR322", "Strategic Studies in the 20th Century"),
                ("INR332", "War and Peace in West Africa Since 1960"),
                ("INR342", "Southern Africa in Global Politics"),
                ("INR352", "International Relations in East and Central Africa"),
                ("INR382", "Nigeria's Foreign Policy II"),

                # Electives
                ("INR372", "Regional Integration and Institutions"),
                ("POL312", "Logic and Methods of Political Inquiry"),
            ],

            (400, "First Semester"): [
                ("INR421", "Seminar Presentation in International and Diplomatic Studies"),
                ("INR431", "International Relations of Francophone West Africa"),
                ("INR441", "Contemporary Strategic Studies"),
                ("INR451", "Introduction to Research Methods in International Relations"),
                ("INR491", "China in World Politics"),
                ("PCR415", "The Nature of Global Terrorism"),

                # Electives
                ("PCR417", "International Relations and Security"),
            ],

            (400, "Second Semester"): [
                ("INR412", "Foreign Policies of Great Powers"),
                ("INR422", "International Institutions"),

                # Electives
                ("INR432", "Afro-Asia Relations"),
                ("INR499", "Research Project / Long Essay"),
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
                "B.Sc. International and Diplomatic Studies courses seeded successfully."
            )
        )