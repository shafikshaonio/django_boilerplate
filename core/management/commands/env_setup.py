from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def handle(self, *args, **kwargs):
        time_zone = str(input(self.style.NOTICE("What is your preferred timezone? (default: 'UTC'): ")))
        database = str(input(self.style.NOTICE("What is your preferred timezone? (default: 'UTC'): ")))
