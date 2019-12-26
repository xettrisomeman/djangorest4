from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Person(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    city = models.CharField( max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    