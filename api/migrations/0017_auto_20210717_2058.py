# Generated by Django 3.2.5 on 2021-07-17 15:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_gsheettable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='college_image',
        ),
        migrations.AddField(
            model_name='college',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='established',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)]),
        ),
        migrations.AddField(
            model_name='college',
            name='facebook',
            field=models.URLField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='college',
            name='full_address',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='college',
            name='instagram',
            field=models.URLField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='college',
            name='linkedin',
            field=models.URLField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='college',
            name='static_map_src',
            field=models.URLField(blank=True, max_length=330),
        ),
        migrations.AddField(
            model_name='college',
            name='twitter',
            field=models.URLField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='college',
            name='youtube',
            field=models.URLField(blank=True, max_length=60),
        ),
    ]
