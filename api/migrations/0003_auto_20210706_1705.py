# Generated by Django 3.2.4 on 2021-07-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210706_1705'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='Timetable',
        ),
    ]
