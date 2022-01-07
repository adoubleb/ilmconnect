from django.db import models
from datetime import datetime

class Assignments(models.Model):
    subject = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    rateperhour = models.IntegerField()
    gender = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    desc = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now)