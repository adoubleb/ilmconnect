# Generated by Django 4.0.1 on 2022-01-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]