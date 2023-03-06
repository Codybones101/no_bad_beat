from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    last_update = models.CharField(max_length=100)
    away_price = models.IntegerField()
    home_price = models.IntegerField()
