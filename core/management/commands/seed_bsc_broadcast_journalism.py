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
    help = "Seed B.Sc. Broadcast Journalism courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Social Sciences"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Broadcast Journalism"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Broadcast Journalism"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("BCJ111", "Introduction to Broadcast Journalism"),
                ("BCJ113", "History of Broadcasting"),
                ("BCJ115", "Introduction to Radio Broadcasting"),
                ("BCJ117", "Introduction to Television Broadcasting"),
                ("MAC111", "Introduction to Mass Communication"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("BCJ112", "Fundamentals of Human Communication"),
                ("BCJ114", "Broadcast Writing and Scripting"),
                ("BCJ116", "Introduction to News Reporting"),
                ("BCJ118", "Introduction to Audio Production"),
                ("BCJ122", "Introduction to Video Production"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("BCJ211", "Radio Production Techniques"),
                ("BCJ213", "Television Production Techniques"),
                ("BCJ215", "Broadcast News Reporting"),
                ("BCJ217", "Broadcast Presentation Skills"),
                ("BCJ219", "Media and Society"),
                ("BCJ221", "Introduction to Photojournalism"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("BCJ212", "News Gathering and Reporting"),
                ("BCJ214", "Broadcast Editing"),
                ("BCJ216", "Feature and Documentary Production"),
                ("BCJ218", "Communication Research Methods"),
                ("BCJ222", "Audio and Video Editing"),
                ("BCJ224", "Introduction to Digital Broadcasting"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("BCJ311", "Advanced Radio Production"),
                ("BCJ313", "Advanced Television Production"),
                ("BCJ315", "Broadcast Journalism Practice"),
                ("BCJ317", "Documentary Production"),
                ("BCJ319", "Media Law and Ethics"),
                ("BCJ321", "International Broadcasting"),
                ("BCJ323", "Development Communication"),
            ],

            (300, "Second Semester"): [
                ("BCJ312", "Investigative Broadcast Reporting"),
                ("BCJ314", "Broadcast Programme Planning"),
                ("BCJ316", "Broadcast Management"),
                ("BCJ318", "Online Journalism and Digital Media"),
                ("BCJ322", "Communication Theory"),
                ("BCJ324", "Broadcast Audience Research"),
                ("BCJ399", "SIWES"),
            ],

            (400, "First Semester"): [
                ("BCJ411", "Advanced Broadcast Reporting"),
                ("BCJ413", "Media Entrepreneurship"),
                ("BCJ415", "Broadcast Station Management"),
                ("BCJ417", "International Broadcast Journalism"),
                ("BCJ419", "Research Project I"),
            ],

            (400, "Second Semester"): [
                ("BCJ412", "Contemporary Issues in Broadcasting"),
                ("BCJ414", "New Media Technologies"),
                ("BCJ416", "Digital Streaming and Content Distribution"),
                ("BCJ418", "Seminar in Broadcast Journalism"),
                ("BCJ420", "Research Project II"),
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
                "B.Sc. Broadcast Journalism courses seeded successfully."
            )
        )