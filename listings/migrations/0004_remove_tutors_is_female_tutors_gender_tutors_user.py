# Generated by Django 4.0.1 on 2022-01-18 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0003_tutors_is_ars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutors',
            name='is_female',
        ),
        migrations.AddField(
            model_name='tutors',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='tutors',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
