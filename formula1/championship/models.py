from django.db import models

from team.models import Driver, Team


class Season(models.Model):

    year = models.IntegerField()


class ConstructorsChampionship(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    position = models.IntegerField()


class DriversChampionship(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
