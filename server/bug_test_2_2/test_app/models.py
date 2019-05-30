from django.db import models
from django.contrib import admin

# Create your models here.
class TestModel(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.first_name) +' '+ str(self.last_name)

class Language(models.Model):
    mother_tongue = models.CharField(max_length = 30)
    person = models.ForeignKey(TestModel, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.mother_tongue)

class Skill(models.Model):
    name = models.CharField(max_length = 30)
    people = models.ManyToManyField(TestModel)

class Customer(models.Model):
    num = models.IntegerField()


class Account(models.Model):
    ACCOUNT_TYPES = (
        (1, 'A'),
        (2, 'B'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_type = models.IntegerField(choices=ACCOUNT_TYPES)

    a = models.CharField(max_length=255, blank=True) # should be edited when type = "A"
    b = models.CharField(max_length=255, blank=True) # should be edited when type = "B"
