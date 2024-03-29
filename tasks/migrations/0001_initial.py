# Generated by Django 4.0.1 on 2022-01-17 10:04

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('subjects', models.CharField(max_length=100)),
                ('locations', multiselectfield.db.fields.MultiSelectField(choices=[('Central', 'Central'), ('East', 'East'), ('North', 'North'), ('Northeast', 'Northeast'), ('West', 'West')], max_length=33)),
                ('level', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('submit_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
