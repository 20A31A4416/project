# Generated by Django 4.1.7 on 2023-06-06 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_apk', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stream',
            name='event',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='time',
        ),
        migrations.DeleteModel(
            name='PlanQuerie',
        ),
    ]
