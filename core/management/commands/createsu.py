from accounts.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='info').exists():
            if not User.objects.filter(email='info@everything-on-amex.com').exists():
                User.objects.create_superuser(
                    username='info',
                    email='info@everything-on-amex.com',
                    password='Nigeria234'
                )
            print('Superuser has been created!.')