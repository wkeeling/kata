from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=100)
    logo = models.ImageField()


class Driver(models.Model):

    name = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.ImageField()

