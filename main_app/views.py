from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from .models import Player, Team, Tournament
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.http import JsonResponse
import requests

#SECTION: Intro templates
class Home(LoginView):
    template_name = 'home.html'

# Change to class-based
def about(req):
    return render(req, 'about.html')

# TODO: Will need to amend this once the API has been integrated

@login_required
def player_detail(req, player_id):
    player = Player.objects.get(id=player_id)
    return render(req, 'players/detail.html', {'player': player})

class CreatePlayer(CreateView):
    model = Player
    fields = '__all__'
    success_url = '/players/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def player_list(req):
    players = Player.objects.all()
    return render(req, 'players/player_list.html', {'players': players})

class PlayerUpdate(UpdateView):
    model = Player
    fields = ['name', 'age', 'team', 'position']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'

#SECTION: Team Routes
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