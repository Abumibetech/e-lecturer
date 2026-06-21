from core.models import (
    Faculty, Department, Programme,
    Level, Semester, Course
)

from core.seed.noun_data.index import NOUN_DATA
from core.seed.base import (
    get_or_create_faculty,
    get_or_create_department,
    get_or_create_programme
)


class NounBuilder:

    def __init__(self):
        self.levels = {
            i: Level.objects.get_or_create(name=i)[0]
            for i in [100, 200, 300, 400, 500]
        }

        self.sem1 = Semester.objects.get_or_create(name="First Semester")[0]
        self.sem2 = Semester.objects.get_or_create(name="Second Semester")[0]

        self.created = 0

    def seed(self):

        for faculty_name, departments in NOUN_DATA.items():

            faculty, _ = get_or_create_faculty(Faculty, faculty_name)

            for dept_name, programmes in departments.items():

                department, _ = get_or_create_department(
                    Department, faculty, dept_name
                )

                for programme_name, levels_data in programmes.items():

                    programme, _ = get_or_create_programme(
                        Programme, department, programme_name
                    )

                    for level, courses in levels_data.items():

                        semester_toggle = True

                        for code, title in courses:

                            semester = self.sem1 if semester_toggle else self.sem2
                            semester_toggle = not semester_toggle

                            Course.objects.get_or_create(
                                programme=programme,
                                level=self.levels[level],
                                semester=semester,
                                code=code,
                                defaults={"title": title}
                            )

                            self.created += 1

        return self.created