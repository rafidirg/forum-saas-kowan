from django.db import models
from django.contrib.auth.models import AbstractUser


class Course(models.Model):
    course_id = models.CharField(max_length=10)
    course_name = models.CharField(max_length=25)

    def __str__(self):
        return self.course_id


class AppUser(AbstractUser):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, null=True)
