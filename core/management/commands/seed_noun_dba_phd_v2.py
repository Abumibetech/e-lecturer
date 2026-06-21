from django.core.management.base import BaseCommand
from core.models import Faculty, Department, Programme, Level, Semester, Course


class Command(BaseCommand):
    help = "Seed NOUN DBA / PhD Business Administration (Refined Version)"

    def handle(self, *args, **kwargs):

        # =========================
        # FACULTY
        # =========================
        faculty, _ = Faculty.objects.get_or_create(
            name="Management Sciences",
            defaults={"slug": "management-sciences"}
        )

        # =========================
        # DEPARTMENT
        # =========================
        department, _ = Department.objects.get_or_create(
            faculty=faculty,
            name="Business Administration",
            defaults={"slug": "business-administration"}
        )

        # =========================
        # PROGRAMME
        # =========================
        programme, _ = Programme.objects.get_or_create(
            department=department,
            name="Doctor of Business Administration (DBA / PhD)"
        )

        # =========================
        # LEVEL
        # =========================
        level900, _ = Level.objects.get_or_create(name=900)

        # =========================
        # SEMESTERS
        # =========================
        first_semester, _ = Semester.objects.get_or_create(name="First Semester")
        second_semester, _ = Semester.objects.get_or_create(name="Second Semester")

        courses = [

            # =====================================
            # DOCTORAL COURSEWORK CORE FOUNDATION
            # =====================================
            (900, first_semester, "GST907", "Advanced Research Methodology and Scholarly Writing"),
            (900, first_semester, "DBA901", "Advanced Managerial Economics Theory"),
            (900, first_semester, "DBA902", "Advanced Financial Management and Corporate Finance"),
            (900, first_semester, "DBA903", "Advanced Organizational Behaviour and Theory"),
            (900, first_semester, "DBA904", "Advanced Marketing Theory and Practice"),
            (900, first_semester, "DBA905", "Advanced Quantitative and Qualitative Research Methods"),
            (900, first_semester, "DBA906", "Strategic Management Theory and Applications"),

            # =====================================
            # ADVANCED DOCTORAL CORE COURSES
            # =====================================
            (900, second_semester, "DBA907", "Corporate Governance and Business Ethics"),
            (900, second_semester, "DBA908", "Operations and Supply Chain Strategy"),
            (900, second_semester, "DBA909", "Human Resource Development and Leadership Theory"),
            (900, second_semester, "DBA910", "International Business Environment and Strategy"),
            (900, second_semester, "DBA911", "Innovation and Knowledge Management Systems"),
            (900, second_semester, "DBA912", "Business Policy and Advanced Strategic Decision Making"),

            # =====================================
            # ELECTIVE COURSES
            # =====================================
            (900, second_semester, "DBA913", "Leadership and Executive Decision Making Theory"),
            (900, second_semester, "DBA915", "Public Sector Management and Policy Analysis"),
            (900, second_semester, "DBA917", "Global Business Strategy and Economic Systems"),
            (900, second_semester, "DBA919", "Risk Management and Corporate Sustainability"),
            (900, second_semester, "DBA921", "Entrepreneurship and Venture Creation Theory"),
            (900, second_semester, "DBA923", "Digital Business Transformation and Analytics"),

            # =====================================
            # SEMINAR COMPONENTS
            # =====================================
            (900, first_semester, "DBA930", "Doctoral Seminar I: Research Proposal Development"),
            (900, second_semester, "DBA932", "Doctoral Seminar II: Theoretical Framework Refinement"),

            # =====================================
            # CANDIDACY EXAMINATION
            # =====================================
            (900, second_semester, "DBA940", "PhD Qualifying Examination (Comprehensive Assessment)"),

            # =====================================
            # RESEARCH PHASE (DISSERTATION STAGE)
            # =====================================
            (900, second_semester, "DBA950", "Dissertation Proposal Defence and Research Residency"),
            (900, second_semester, "DBA999", "PhD Thesis / Doctoral Dissertation in Business Administration"),
        ]

        levels = {
            900: level900,
        }

        created = 0

        for level_num, semester, code, title in courses:

            obj, was_created = Course.objects.get_or_create(
                programme=programme,
                level=levels[level_num],
                semester=semester,
                code=code,
                defaults={
                    "title": title,
                    "description": title,
                }
            )

            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully seeded DBA/PhD Business Administration (v2): {created} courses"
            )
        )