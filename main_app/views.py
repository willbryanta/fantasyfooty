from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from .models import Player, Team, FantasyTeam
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import JsonResponse
from .services.api_service import fetch_player_data

import requests
import http.client


#SECTION: Intro templates
class Home(LoginView):
    template_name = 'home.html'

# Change to class-based
def about(req):
    return render(req, 'about.html')

#SECTION: Player routes
@login_required
def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)

    return render(request, 'players/detail.html', {'player': player})

class CreatePlayer(LoginRequiredMixin, CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# @login_required
# def player_list(req):
#     players = Player.objects.all()
#     return render(req, 'players/player_list.html', {'players': players})

@login_required
def player_list(request):
    try:
        api_data = fetch_player_data(api_id=22)

        players = api_data.get('athletes',[])

        print(players)


        if not isinstance(players, list):
            players = []

        print(players)
    except Exception as e:
        players = []
        print(f"Error fetching player data: {e}")
    
    return render(request, 'players/player_list.html', {'players': players})

class PlayerUpdate(LoginRequiredMixin, UpdateView):
    model = Player
    fields = ['name', 'age', 'team', 'position']

class PlayerDelete(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/players/'

#SECTION: Team Routes
class TeamCreate(LoginRequiredMixin, CreateView):
    model = Team
    fields = '__all__'

class TeamList(ListView):
    model = Team

class TeamDetail(DetailView):
    model = Team

class TeamUpdate(LoginRequiredMixin, UpdateView):
    model = Team
    fields = '__all__'

class TeamDelete(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = '/teams/'

#SECTION:
@login_required
def add_player_to_fantasy_team(req, player_id):
    player = get_object_or_404(Player, id=player_id)
    fantasy_team, created = FantasyTeam.objects.get_or_create(user=req.user)
    if player not in fantasy_team.players.all():
        fantasy_team.players.add(player)
        return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players })
    return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players})

def remove_player_from_fantasy_team(req, player_id):
    player = get_object_or_404(Player, id=player_id)
    fantasy_team = FantasyTeam.objects.get(user=req.user)
    if player in fantasy_team.players.all():
        fantasy_team.players.remove(player)
        return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players })
    return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players})
        
@login_required
def my_team_list(req):
    fantasy_team, created = FantasyTeam.objects.get_or_create(user=req.user)
    players = fantasy_team.players.all()
    return render(req, 'team/team_list.html', {'players': players })

#SECTION: signup
def signup(req):
    error_message = ''
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message }
    return render(req, 'signup.html', context)