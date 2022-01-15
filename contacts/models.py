from django.db import models
from datetime import datetime

class Contact(models.Model):
  tutor = models.CharField(max_length=200)
  tutor_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  subject = models.CharField(max_length=100, default=None)
  level = models.CharField(max_length=100, default=None)
  location = models.CharField(max_length=100, default=None)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.name
