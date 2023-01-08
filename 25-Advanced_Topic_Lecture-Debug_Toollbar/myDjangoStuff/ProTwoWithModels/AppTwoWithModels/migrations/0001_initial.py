# Generated by Django 3.0.3 on 2020-06-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, unique=True)),
                ('last_name', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
