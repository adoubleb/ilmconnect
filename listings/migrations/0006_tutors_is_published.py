# Generated by Django 4.0.1 on 2022-01-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_tutors_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutors',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]