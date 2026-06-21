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
    help = "Seed French Programme courses"

    def handle(self, *args, **kwargs):

        faculty, _ = Faculty.objects.get_or_create(
            name="Arts"
        )

        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="French"
        )

        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="B.A. French"
        )

        courses = {

            # =========================
            # 100 LEVEL FIRST SEMESTER
            # =========================
            (100, "First Semester"): [

                ("GST101", "Use of English and Communication Skills I"),
                ("GST103", "Computer Fundamentals"),
                ("GST105", "History and Philosophy of Science"),
                ("GST107", "A Study Guide for the Distance Learner"),
                ("EDU111", "Foundations of Education"),
                ("FRE111", "Language Laboratory Work / Oral French"),
                ("FRE121", "French Grammar I"),
                ("FRE131", "Textual Analysis I"),
                ("FRE141", "Introduction to Composition Writing in French"),
            ],

            # ==========================
            # 100 LEVEL SECOND SEMESTER
            # ==========================
            (100, "Second Semester"): [

                ("GST102", "Use of English and Communication Skills II"),
                ("GST104", "Use of the Library"),
                ("EDU112", "Professionalism in Teaching"),
                ("EDU114", "History of Education in Nigeria"),
                ("FRE112", "Oral and Aural Comprehension"),
                ("FRE122", "French Grammar II"),
                ("FRE132", "Textual Analysis II"),
                ("FRE162", "Introduction to Francophone African Culture and Civilisation"),
            ],

            # =========================
            # 200 LEVEL FIRST SEMESTER
            # =========================
            (200, "First Semester"): [

                ("GST201", "Nigerian People and Culture"),
                ("EDU231", "Curriculum Development Theory and Practice"),
                ("EDU233", "General Teaching Methods"),
                ("FRE211", "Advanced Studies in Oral and Written Comprehension I"),
                ("FRE221", "French Grammar and Composition I"),
                ("FRE231", "Introduction to French Phonology"),
                ("FRE241", "Introduction to French Literary Genre I (Prose)"),
                ("FRE271", "Introduction to Francophone African Literature (Prose, Poetry and Drama)"),
            ],

            # ==========================
            # 200 LEVEL SECOND SEMESTER
            # ==========================
            (200, "Second Semester"): [

                ("GST202", "Fundamentals of Peace Studies and Conflict Resolution"),
                ("GST204", "Entrepreneurship and Innovation"),
                ("EDU212", "Sociology of Education"),
                ("EDU214", "Philosophy of Education"),
                ("EDU216", "Special Methods (Micro Teaching and School Visits)"),
                ("EDU222", "French Language Methods"),
                ("FRE202", "Advanced Studies in Oral and Written Comprehension in French II"),
                ("FRE212", "Advanced Oral French"),
                ("FRE222", "French Grammar and Composition II"),
                ("FRE242", "Introduction to French Literary Genres II (Drama and Poetry)"),
                ("FRE252", "Critical Appreciation of Literature"),
            ],

            # =========================
            # 300 LEVEL FIRST SEMESTER
            # =========================
            (300, "First Semester"): [

                ("EDU321", "Psychology of Learning"),
                ("EDU323", "Basic Research Methods in Education"),
                ("EDU335", "Teaching Practice I"),
                ("FRE301", "Theory and Practice of Translation"),
                ("FRE311", "Advanced Formal and Informal Writing in French I"),
                ("FRE321", "Advanced Studies in French Language Structure I"),
                ("FRE331", "Advanced Studies in French Phonetics"),
                ("FRE341", "Oral Communicative Skills in French I"),
            ],

            # ==========================
            # 300 LEVEL SECOND SEMESTER
            # ==========================
            (300, "Second Semester"): [

                ("GST302", "Business Creation and Growth"),
                ("EDU314", "Comparative Education"),
                ("EDU332", "Introduction to Educational Technology"),
                ("EDU336", "Post Teaching Practice Evaluation / Remediation"),
                ("FRE302", "Advanced Studies in Translation (Theme et Version)"),
                ("FRE312", "Advanced Formal and Informal Writing in French II"),
                ("FRE322", "Advanced Studies in French Language Structure II"),
                ("FRE342", "Oral Communication Skills in French II"),
            ],

            # =========================
            # 400 LEVEL FIRST SEMESTER
            # =========================
            (400, "First Semester"): [

                ("EDU421", "Guidance and Counselling"),
                ("EDU423", "Measurement and Evaluation"),
                ("EDU435", "Teaching Practice II"),
                ("FRE421", "Advanced Studies in French Language Structure III"),
                ("FRE423", "Linguistics Applied to the Teaching of French"),
                ("FRE451", "Advanced Translation I"),
                ("FRE461", "Applied Linguistics"),
            ],

            # ==========================
            # 400 LEVEL SECOND SEMESTER
            # ==========================
            (400, "Second Semester"): [

                ("EDU412", "Educational Management"),
                ("EDU426", "Special Education"),
                ("EDU420", "Research Project"),
                ("FRE422", "Advanced Studies in French Language Structure IV"),
                ("FRE432", "Francophone African Literature (Theatre and Poetry)"),
                ("FRE452", "Advanced Translation II"),
                ("FRE472", "Pre- and Post-Independence Francophone Literature (Poetry)"),
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
                "French programme courses seeded successfully."
            )
        )