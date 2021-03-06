# Generated by Django 3.2.5 on 2021-07-07 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('branch_code', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('course_code', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('subject_code', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('year', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('THIRD', 'THIRD'), ('FOURTH', 'FOURTH')], default='FIRST', max_length=8)),
                ('semester', models.CharField(choices=[('SEM_1', 'I Semester'), ('SEM_2', 'II Semester'), ('SEM_3', 'III Semester'), ('SEM_4', 'IV Semester'), ('SEM_5', 'V Semester'), ('SEM_6', 'VI Semester'), ('SEM_7', 'VII Semester'), ('SEM_8', 'VIII Semester')], default='FIRST', max_length=5)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='timetables', to='api.branch')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='timetables', to='api.course')),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=60)),
                ('link', models.URLField()),
                ('cover_image', models.URLField()),
                ('year', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('THIRD', 'THIRD'), ('FOURTH', 'FOURTH')], default='FIRST', max_length=8)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='textbooks', to='api.branch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='textbooks', to='api.course')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='textbooks', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='textbooks', to='api.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], default='MON', max_length=3)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('teacher', models.CharField(max_length=60)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subject')),
                ('timetables', models.ManyToManyField(related_name='lectures', to='api.Timetable')),
            ],
        ),
    ]
