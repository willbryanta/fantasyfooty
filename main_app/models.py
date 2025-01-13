from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# TODO: Check with Foad whether the player instances should be initialised with the following or whether 

# class Player(models.Model)
#         def __init__(self, name, age, years_played, position, team, headshotURL):
#             self.name = name
#             self.age = age
#             self.years_played = years_played
#             self.position = position
#             self.team = team
#             self.headshotURL = headshotURL

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
        return reverse("player-detail", kwargs={"pk": self.id})
    
class Owner(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("owner-detail", kwargs={"pk": self.id})
    
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
class Team(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    colors = models.CharField(max_length=2, choices=COLORS, default=COLORS[0][0])

    def __str__(self):
        return f'{self.name} ({self.get_colors_display()} from {self.state})'

    def get_absolute_url(self):
        return reverse("team-detail", kwargs={"pk": self.id})
    
