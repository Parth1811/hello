from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    phone  = models.CharField(max_length=10)


class Batch(models.Model):
    batch_code =  models.CharField(max_length=10)

    def __str__(self):
        return self.batch_code

class Teacher(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    batch_id = models.ManyToManyField(Batch)

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll_no = models.IntegerField()
    batch_id = models.ManyToManyField(Batch)

    def __str__(self):
        return self.user.username
