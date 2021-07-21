from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "This command is responsible for generating fake Vehicles data"

    def handle(self, *args, **options):
        pass
