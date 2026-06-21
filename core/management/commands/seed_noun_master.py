from django.core.management.base import BaseCommand
from core.seed.builder import NounBuilder


class Command(BaseCommand):
    help = "MASTER NOUN SEEDER (ALL FACULTIES)"

    def handle(self, *args, **kwargs):

        builder = NounBuilder()
        created = builder.seed()

        self.stdout.write(self.style.SUCCESS(
            f"🔥 MASTER NOUN SEED COMPLETE → {created} courses created"
        ))