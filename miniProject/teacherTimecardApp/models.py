from django.db import models
from django.utils import timezone

# Create your models here.
class TimeCard(models.Model):
    teacherName=models.CharField(max_length=200)
    school=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    hours=models.IntegerField(default=0)
    dateofWork=models.DateField(default=timezone.now())
    dateofEntry=models.DateField(default=timezone.now())
