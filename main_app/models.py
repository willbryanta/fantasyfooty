from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# TODO: Delete once API integration is done
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
    
class Athlete(models.Model):
    uid = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=200)
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    date_of_birth = models.DateTimeField()
    jersey = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    headshot_url = models.URLField(null=True, blank=True)

class Link(models.Model):
    athlete = models.ForeignKey(Athlete, related_name='links', on_delete=models.CASCADE)
    rel = models.CharField(max_length=50)
    href = models.URLField()
    text = models.CharField(max_length=100)

COLORS = (
    ('Bl', 'Black'),
    ('W', 'White'),
    ('Gr', 'Grey'),
    ('R', 'Red'),
    ('O', 'Orange'),
    ('Y', 'Yellow'),
    ('G', 'Green'),
    ('B', 'Blue'),
    ('I', 'Indigo'),
    ('V', 'Violet')
)

# E.g. Tampa Bay Buccaneers
class Team(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    colors = models.CharField(max_length=2, choices=COLORS, default=COLORS[0][0])

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