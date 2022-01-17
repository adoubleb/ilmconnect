from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import BooleanField
from multiselectfield import MultiSelectField
from datetime import datetime
class Task(models.Model):

    LEVEL_CHOICES = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary'),
    ('Pre-U/JC', 'Pre-U/JC'),
    )

    LOCATION_CHOICES = (
    ('Central', 'Central'),
    ('East','East'),
    ('North','North'),
    ('Northeast','Northeast'),
    ('West','West'),
    )
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subjects = models.CharField(max_length=100)
    locations = MultiSelectField(choices = LOCATION_CHOICES)
    level = models.CharField(max_length=50)
    rate = models.IntegerField()
    description = models.TextField(blank=True)
    submit_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)