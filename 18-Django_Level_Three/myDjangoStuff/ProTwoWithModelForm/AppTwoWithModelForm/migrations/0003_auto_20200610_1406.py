# Generated by Django 3.0.3 on 2020-06-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwoWithModelForm', '0002_remove_mymodel_conf_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
