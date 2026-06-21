from django.utils.text import slugify

def get_or_create_faculty(model, name):
    return model.objects.get_or_create(
        name=name,
        defaults={"slug": slugify(name)}
    )

def get_or_create_department(model, faculty, name):
    return model.objects.get_or_create(
        name=name,
        faculty=faculty,
        defaults={"slug": slugify(name)}
    )

def get_or_create_programme(model, department, name):
    return model.objects.get_or_create(
        name=name,
        department=department
    )