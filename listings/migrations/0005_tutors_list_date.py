# Generated by Django 4.0.1 on 2022-01-18 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_remove_tutors_is_female_tutors_gender_tutors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutors',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
