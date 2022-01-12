from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields import BooleanField
from multiselectfield import MultiSelectField
class Tutors(models.Model):
  SUBJECT_CHOICES = (
    ('Quran', 'Quran'),
    ('Arabic', 'Arabic'),
    ('Malay', 'Malay'),
    ('English','English'),
    ('Maths','Maths'),
    ('Science','Science'),
    ('Chemistry','Chemistry'),
    ('Biology','Biology'),
    ('Physics','Physics'),
    ('Ukhrawi Subjects','Ukhrawi Subjects'),
    ('E-Maths','E-Maths'),
    ('A-Maths','A-Maths'),
  )

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

  name = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  years_experience = models.IntegerField()
  education = models.CharField(max_length=256)
  subjects = MultiSelectField(choices = SUBJECT_CHOICES)
  locations = MultiSelectField(choices = LOCATION_CHOICES)
  levels = MultiSelectField(choices = LEVEL_CHOICES)
  is_female = BooleanField()
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_ars = BooleanField(default=True)
  def __str__(self):
    return self.name