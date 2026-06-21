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
    help = "Seed B.Sc. Criminology and Security Studies courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Criminology and Security Studies"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Criminology and Security Studies"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("CSS111", "Introduction to Sociology"),
                ("CSS121", "Introduction to Psychology"),
                ("CSS131", "Introduction to Political Science"),
                ("CSS133", "Introduction to Criminology I"),
                ("PCR111", "Introduction to Peace Studies"),
                ("PCR114", "Introduction to Conflict Resolution"),
                ("POL111", "Elements of Political Science"),
                ("ECO121", "Principles of Economics I"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("CSS122", "Social Problems and Social Deviance"),
                ("CSS132", "Introduction to Public Administration"),
                ("CSS134", "Introduction to Criminology II"),
                ("CSS124", "Introduction to Anthropology"),
                ("CSS112", "Nigerian Heritage and Culture"),
                ("ECO122", "Principles of Economics II"),
                ("POL112", "Introduction to Nigerian Government and Politics"),
                ("PCR112", "Introduction to Conflict and Peace Studies"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("CSS211", "Sociology of Crime and Delinquency"),
                ("CSS221", "Introduction to Security Studies"),
                ("CSS231", "Criminal Justice System"),
                ("CSS241", "Victimology"),
                ("CSS243", "Criminological Theories"),
                ("JIL211", "Nigerian Legal System I"),
                ("PCR271", "Introduction to Mediation"),
                ("MAC211", "Fundamentals of Mass Communication"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("CSS212", "Sociology of Punishment and Corrections"),
                ("CSS242", "Measurement and Patterns of Crime"),
                ("CSS244", "Types and Analysis of Security Threats"),
                ("CSS246", "Legal and Social Framework of Private Security"),
                ("CSS252", "Intelligence and Security Management"),
                ("MAC212", "Media and Society"),
                ("JIL212", "Nigerian Legal System II"),
                ("PCR272", "Concepts and Practice of Peace Building"),
                ("PCR274", "Introduction to Conflict Transformation"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("CSS331", "Methods of Social Research"),
                ("CSS341", "Policing and Law Enforcement in Nigeria"),
                ("CSS343", "Information System Security Management"),
                ("CSS351", "Prisons and Correction of Offenders"),
                ("CSS361", "Juvenile Institutions and Juvenile Corrections"),
                ("CSS381", "Domestic Violence"),
                ("PUL341", "Criminal Law I"),
                ("PCR373", "Demobilisation, Disarmament and Reintegration"),
            ],

            (300, "Second Semester"): [
                ("CSS332", "Research Methods and Data Analysis"),
                ("CSS342", "Safety Management for Loss Prevention"),
                ("CSS352", "Theory of Crime and Crime Control"),
                ("CSS354", "Special Categories of Offenders"),
                ("CSS356", "Traditional and Informal Mechanisms of Crime Control"),
                ("CSS382", "Terrorism and Counter-Terrorism Studies"),
                ("PUL342", "Criminal Law II"),
                ("PCR362", "Urban Violence and Security"),
            ],

            (400, "First Semester"): [
                ("CSS411", "Contemporary Issues in Criminology"),
                ("CSS431", "Field Observation"),
                ("CSS441", "Technical and Electronics Aspects of Security"),
                ("CSS443", "Traffic and Road Safety Equipment"),
                ("CSS455", "Forensic Science"),
                ("CSS461", "Criminology I"),
                ("CSS491", "Emergency, Riot and Disaster Control"),
                ("PUL241", "Human Rights Law I"),
                ("PCR375", "Language and Information Management in Peace and Conflict Resolution"),
                ("ENG453", "Language and National Development"),
            ],

            (400, "Second Semester"): [
                ("CSS412", "Comparative Criminal Justice Systems"),
                ("CSS442", "Security Planning and Risk Assessment"),
                ("CSS452", "Cybercrime and Digital Security"),
                ("CSS462", "Criminology II"),
                ("CSS492", "Project"),
                ("PUL242", "Human Rights Law II"),
                ("PCR476", "Peace and Security in Africa"),
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
                "B.Sc. Criminology and Security Studies courses seeded successfully."
            )
        )