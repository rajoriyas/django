# Generated by Django 3.0.3 on 2020-06-10 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwoWithModelForm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='conf_email',
        ),
    ]
