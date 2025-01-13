from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from .models import Player, Owner, Team

class Home(LoginView):
    template_name = 'home.html'

# Change to class-based
def about(req):
    return render(req, 'about.html')

def player_list(req):
    players = Player.objects.order_by('-age')
    return render(req, 'players/index.html', {'players': players})

class CreatePlayer(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

def player_detail(req, player_id):
    player = Player.objects.get(id=player_id)

    return render(req, 'players/detail.html', {'player': player})

class PlayerList(ListView):
    model = Player

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'age', 'team', 'position']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class TeamList(ListView):
    model = Team

class TeamDetail(DetailView):
    model = Team

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    success_url = '/teams/'