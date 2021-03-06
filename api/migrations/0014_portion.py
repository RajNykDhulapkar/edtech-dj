# Generated by Django 3.2.5 on 2021-07-11 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_delete_portion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.college')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.subject')),
            ],
        ),
    ]
