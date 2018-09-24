# Generated by Django 2.1.1 on 2018-09-23 10:21

from django.db import migrations


def create_initial_data(apps, schema_editor):
    Season = apps.get_model('championship', 'Season')
    Season.objects.create(
        year=2017
    )


class Migration(migrations.Migration):

    dependencies = [
        ('championship', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data)
    ]