# Generated by Django 2.1.7 on 2019-03-25 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fashionapp', '0002_clothe_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothe_type',
            name='clothe',
        ),
        migrations.DeleteModel(
            name='Clothe_type',
        ),
    ]
