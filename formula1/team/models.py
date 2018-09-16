from django.db import models


class Team(models.Model):

    name = models.CharField()
    logo = models.ImageField()


class Driver(models.Model):

    name = models.CharField()
    dob = models.DateField()
    image = models.ImageField()

