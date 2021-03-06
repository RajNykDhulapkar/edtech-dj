# Generated by Django 3.2.5 on 2021-07-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20210720_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('recommended_by', models.CharField(max_length=60)),
                ('link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='description',
        ),
        migrations.AlterField(
            model_name='faculty',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
