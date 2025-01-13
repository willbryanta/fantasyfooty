from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'), # Change to class-based
    path('players/', views.Players.as_view(), name='players')
]