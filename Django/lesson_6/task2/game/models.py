from django.db import models


class Player(models.Model):
    player_id = models.CharField(max_length=100, verbose_name='id игрока')

    def __str__(self):
        return self.player_id


class Game(models.Model):
    game_id = models.CharField(max_length=100, verbose_name='id игры')
    playing = models.BooleanField(verbose_name='Игра завершена', default=True)
    number = models.IntegerField(null=True)
    players = models.ManyToManyField(Player, through='PlayerGameInfo')

    def __str__(self):
        return self.game_id


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    lifes = models.IntegerField(null=True)
    author = models.BooleanField(verbose_name='автор', default=False)