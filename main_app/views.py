from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from .models import Player, Team, FantasyTeam
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import JsonResponse
from .services.api_service import fetch_player_data, fetch_team_data

import requests
import http.client


#SECTION: Intro templates
class Home(LoginView):
    try:
        template_name = 'home.html'
    except Exception as e:
        return print(f"Error loading home page: {e}")

# Change to class-based
def about(req):
    try:
        return render(req, 'about.html')
    except Exception as e:
        return print(f"Error loading about page: {e}")

#SECTION: Player routes
@login_required
def player_detail(request, player_id):
    try:
        player_details = Player.objects.get(id=player_id)
        return render(request, 'players/detail.html', {'player': player})
    except Exception as e:
        context['players'] = []
        return print(f"Error loading player details: {e}")


class CreatePlayer(LoginRequiredMixin, CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

    try:
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
    except Exception as e:
        return print(f"Error creating player: {e}")

@login_required
def player_list(request):
    try:
        api_data = fetch_player_data(api_id=22)
        players = api_data.get('athletes',[])

        print(players[0])

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
    template_name = 'team_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            api_data = fetch_team_data()
            context['teams'] = api_data[0]['team']
            print(context['teams'])
        except Exception as e:
            context['teams'] = []
            print(f"Error fetching team data: {e}")
        return context
    

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

    try:
        if player not in fantasy_team.players.all():
            fantasy_team.players.add(player)
            return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players })
        return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players})
    except Exception as e:
        return print(f"Error adding player with id: {player_id} to your team")

def remove_player_from_fantasy_team(req, player_id):
    player = get_object_or_404(Player, id=player_id)
    fantasy_team = FantasyTeam.objects.get(user=req.user)

    try:
        if player in fantasy_team.players.all():
            fantasy_team.players.remove(player)
            return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players })
        return render(req, 'team/team_list.html',{"fantasy_team": fantasy_team.players})
    except Exception as e:
        return print(f"Error removing player with id: {player_id} from your team")
        
@login_required
def my_team_list(req):
    fantasy_team, created = FantasyTeam.objects.get_or_create(user=req.user)
    players = fantasy_team.players.all()
    try:
        return render(req, 'team/my_team_list.html', {'players': players })
    except Exception as e:
        return print(f"Error fetching your team list: {e}")

#SECTION: signup
def signup(req):
    error_message = ''

    try:
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
    except Exception as e:
        return print(f"Error signing up: {e}")