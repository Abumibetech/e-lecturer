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
    help = "Seed B.Sc. Film Production courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Faculty of Arts / Media Studies"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Film Production"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.Sc. Film Production"
        )

        courses = {

            (100, "First Semester"): [
                ("GST101", "Use of English and Communication Skills I"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "The Good Study Guide"),
                ("CIT101", "Computers in Society"),
                ("FMC111", "Introduction to Film Production"),
                ("FMC113", "Introduction to Visual Communication"),
                ("FMC115", "History of Cinema"),
                ("FMC117", "Introduction to Screen Storytelling"),
            ],

            (100, "Second Semester"): [
                ("GST102", "Use of English and Communication Skills II"),
                ("CIT102", "Software Application Skills"),
                ("FMC112", "Fundamentals of Human Communication"),
                ("FMC114", "Film Language and Narrative"),
                ("FMC116", "Elements of Film Production"),
                ("FMC118", "Introduction to Scriptwriting"),
                ("FMC132", "Media, Culture and Films"),
            ],

            (200, "First Semester"): [
                ("GST201", "Nigerian Peoples and Culture"),
                ("GST203", "Introduction to Philosophy and Logic"),
                ("FMC211", "Cinematography I"),
                ("FMC213", "Directing for Film"),
                ("FMC215", "Film Editing I"),
                ("FMC217", "Films and Aesthetics Theory"),
                ("FMC219", "Sound for Film Production"),
                ("FMC221", "Introduction to Documentary Production"),
            ],

            (200, "Second Semester"): [
                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("FMC212", "Cinematography II"),
                ("FMC214", "Film Production Management"),
                ("FMC216", "Screenwriting for Film"),
                ("FMC218", "Documentary Film Production"),
                ("FMC222", "Film Criticism and Appreciation"),
                ("FMC224", "Production Design"),
            ],

            (300, "First Semester"): [
                ("GST302", "Business Creation and Growth"),
                ("FMC311", "Advanced Cinematography"),
                ("FMC313", "Film Directing and Production"),
                ("FMC315", "Advanced Screenwriting"),
                ("FMC317", "Film Editing II"),
                ("FMC319", "Documentary Theory and Practice"),
                ("FMC321", "African Cinema"),
                ("FMC323", "Film Law and Ethics"),
            ],

            (300, "Second Semester"): [
                ("FMC312", "Digital Film Production"),
                ("FMC314", "Special Effects and Visual Effects"),
                ("FMC316", "Multimedia Storytelling"),
                ("FMC318", "Film Marketing and Distribution"),
                ("FMC322", "Research Methods in Film Studies"),
                ("FMC324", "Contemporary Film Theory"),
                ("FMC399", "SIWES"),
            ],

            (400, "First Semester"): [
                ("FMC411", "Advanced Film Production"),
                ("FMC413", "Film Entrepreneurship"),
                ("FMC415", "Feature Film Production"),
                ("FMC417", "Film Festival Studies"),
                ("FMC419", "Research Project I"),
                ("FMC421", "Advanced Cinematography and Lighting"),
            ],

            (400, "Second Semester"): [
                ("FMC412", "Contemporary Issues in Film Production"),
                ("FMC414", "Digital Post-Production"),
                ("FMC416", "Film Industry Studies"),
                ("FMC418", "Seminar in Film Production"),
                ("FMC420", "Research Project II"),
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
                "B.Sc. Film Production courses seeded successfully."
            )
        )