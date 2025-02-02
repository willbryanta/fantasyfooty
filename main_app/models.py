from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    years_played = models.IntegerField()
    position = models.CharField(max_length=20)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='players')
    headshotURL = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("player-detail", kwargs={"player_id": self.id})

class Team(models.Model):
    displayName = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    location = models.CharField(max_length=30)
    color = models.Charfield(max_length=30)
    alternate_color = models.Charfield(max_length=20)
    logo = models.models.URLField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.get_colors_display()} from {self.state})'

    def get_absolute_url(self):
        return reverse("team-detail", kwargs={"pk": self.id})

# This is the team that the user owns
class FantasyTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fantasy_team')
    players = models.ManyToManyField(Player, related_name='fantasy_teams')

    def __str__(self):
        return f"{self.user.username}'s Fantasy Team"