from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Run makemigrations and migrate on Render'

    def handle(self, *args, **kwargs):
        call_command('makemigrations')
        call_command('migrate')
        self.stdout.write(self.style.SUCCESS("✅ Migrations applied successfully on Render."))
