import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project_with_models.settings')

import django
django.setup()

import random
from first_app_with_models.models import Topic, Webpage, AccessRecord
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topics():
    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topic.save()
    return topic

def populate(N=5):
    for entry in range(N):
        top = add_topics()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpge = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        webpge.save()

        acc_rcd = AccessRecord.objects.get_or_create(name=webpge, date=fake_date)[0]
        acc_rcd.save()

if __name__ == '__main__':
    print('Populate Script')
    populate(20)
    print('Completed!')
