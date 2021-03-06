# Generated by Django 3.2.5 on 2021-07-16 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_portion_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gsheettable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('gsheet_src', models.URLField(max_length=250)),
                ('year', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('THIRD', 'THIRD'), ('FOURTH', 'FOURTH')], default='FIRST', max_length=8)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='gsheettables', to='api.branch')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='gsheettables', to='api.college')),
            ],
        ),
    ]
