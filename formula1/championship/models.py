from django.db import models

from team.models import Driver, Team


class Season(models.Model):

    class Meta:
        ordering = ('-year', )

    year = models.IntegerField()


class ConstructorsChampionshipResult(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='constructor_results')
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
    position = models.IntegerField()


class DriversChampionshipResult(models.Model):

    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='driver_results')
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
