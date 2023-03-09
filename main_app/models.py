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
    comment_date = models.DateField(auto_now_add=True, blank=True)
    comment = models.TextField(max_length=250)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


class Bet(models.Model):
    bet_user = models.CharField(max_length=100)
    team_picked = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    bet_size = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)