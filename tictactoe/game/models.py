from django.db import models

class Game(models.Model):
    game_id = models.CharField(max_length=50, unique=True)
    board = models.CharField(max_length=9, default=' ' * 9)
    next_move = models.CharField(max_length=1, default='X')
    winner = models.CharField(max_length=1, null=True, blank=True)
