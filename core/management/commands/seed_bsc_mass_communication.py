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
    help = "Seed B.Sc. Mass Communication courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Mass Communication"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Mass Communication"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("MAC111", "Introduction to Mass Communication"),
                ("MAC113", "History of Nigerian Mass Media"),
                ("MAC115", "African Communication Systems I"),
                ("MAC117", "Writing for Mass Media I"),
                ("MAC121", "Introduction to News Writing and Reporting"),

                # Electives
                ("ENG121", "Structure of Modern English I"),
                ("CSS111", "Introduction to Sociology"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("MAC112", "Fundamentals of Human Communication"),
                ("MAC114", "African Communication Systems II"),
                ("MAC118", "Writing for Mass Media II"),
                ("MAC122", "News Reporting and Writing"),
                ("MAC124", "Introduction to Radio and Television"),

                # Electives
                ("INR112", "Introduction to Law and Diplomacy in Pre-Colonial Africa"),
                ("CSS112", "Introduction to Psychology"),
                ("ENG122", "Structure of Modern English II"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("MAC211", "Feature Writing"),
                ("MAC213", "Introduction to Public Relations"),
                ("MAC215", "Introduction to Advertising"),
                ("MAC217", "Editing and Graphics of Communication"),
                ("MAC219", "Introduction to Photojournalism"),
                ("MAC221", "Media and Society"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("MAC212", "Public Affairs Reporting"),
                ("MAC214", "Public Relations Writing"),
                ("MAC216", "Advertising Copy Writing and Visualization"),
                ("MAC218", "Newspaper and Magazine Production"),
                ("MAC222", "Radio and Television Production"),
                ("MAC224", "Communication Research Methods"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("MAC311", "Investigative Reporting"),
                ("MAC313", "Public Relations Campaigns"),
                ("MAC315", "Advertising Campaign Planning"),
                ("MAC317", "Broadcast Journalism"),
                ("MAC319", "International Communication"),
                ("MAC321", "Media Law and Ethics"),
                ("MAC323", "Development Communication"),
            ],

            (300, "Second Semester"): [
                ("MAC312", "Editorial Writing"),
                ("MAC314", "Public Relations Practice"),
                ("MAC316", "Advertising Management"),
                ("MAC318", "Television Programme Production"),
                ("MAC322", "Communication Theory"),
                ("MAC324", "Online Journalism"),
                ("MAC399", "SIWES"),
            ],

            (400, "First Semester"): [
                ("MAC411", "Advanced Reporting"),
                ("MAC413", "Media Management"),
                ("MAC415", "Development Journalism"),
                ("MAC417", "International Public Relations"),
                ("MAC419", "Mass Communication Research Project I"),
            ],

            (400, "Second Semester"): [
                ("MAC412", "Contemporary Issues in Mass Communication"),
                ("MAC414", "Media Entrepreneurship"),
                ("MAC416", "New Media Technologies"),
                ("MAC418", "Mass Communication Research Project II"),
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
                "B.Sc. Mass Communication courses seeded successfully."
            )
        )