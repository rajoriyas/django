import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwoWithModels.settings')

import django
django.setup()

from faker import Faker
faker = Faker()

from AppTwoWithModels.models import User

def add_data(N=5):
    for n in range(N):
        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_email = faker.email()

        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        user.save()

if __name__ == '__main__':
    print('Population with Faker')
    add_data(20)
    print('Successful completed')
