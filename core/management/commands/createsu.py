from accounts.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@everything-on-amex.com').exists():
            User.objects.create_superuser(
                email='admin@everything-on-amex.com',
                password='Ejigbo234'
            )
        print('Superuser has been created.')