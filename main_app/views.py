from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

# Change to class-based
def about(req):
    return render(req, 'about.html')

