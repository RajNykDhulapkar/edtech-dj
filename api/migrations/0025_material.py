# Generated by Django 3.2.5 on 2021-07-17 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0024_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField()),
                ('author', models.CharField(max_length=60)),
                ('year', models.CharField(choices=[('FIRST', 'FIRST'), ('SECOND', 'SECOND'), ('THIRD', 'THIRD'), ('FOURTH', 'FOURTH')], default='FIRST', max_length=8)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.branch')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.course')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='materials', to='api.subject')),
            ],
        ),
    ]
