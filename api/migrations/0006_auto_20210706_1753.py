# Generated by Django 3.2.5 on 2021-07-06 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_course_course_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='code',
            new_name='subject_code',
        ),
        migrations.AddField(
            model_name='textbook',
            name='branch_code',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='textbook',
            name='course_code',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='textbook',
            name='year',
            field=models.CharField(default='', max_length=8),
        ),
    ]
