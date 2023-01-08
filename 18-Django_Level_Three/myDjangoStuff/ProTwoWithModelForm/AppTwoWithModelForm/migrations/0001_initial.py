# Generated by Django 3.0.3 on 2020-06-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]