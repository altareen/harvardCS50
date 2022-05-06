from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Department(models.Model):
    name = models.CharField(max_length=30)

class Course(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher")
    capacity = models.IntegerField(default=0)
    section = models.IntegerField(default=0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="area")
    students = models.ManyToManyField(User, blank=True, related_name="pupils")

