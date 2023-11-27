from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Admin',
            last_name='Adminov',
            #char_id='2345678',
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        user.set_password('qwerty12345'),
        user.save()
