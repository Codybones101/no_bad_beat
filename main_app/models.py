from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.CharField(max_length=100)
    game_date = models.DateField(blank=True)
    away_team = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    away_price = models.IntegerField()
    home_price = models.IntegerField()

    
class Comment(models.Model):
    comment_user = models.CharField(max_length=100)
    comment_date = models.DateField(blank=True)
    comment = models.TextField(max_length=250)