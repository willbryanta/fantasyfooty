from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('players/', views.player_list, name='player-list'),
    path('players/<int:player_id>/', views.player_detail, name='player-detail'),
    path('players/create/', views.CreatePlayer.as_view(), name='create-player'),
    path('players/<int:pk>/update/', views.PlayerUpdate.as_view(), name='player-update'),
    path('players/<int:pk>/delete/', views.PlayerDelete.as_view(), name='player-delete'),
    path('my-team/', views.my_team_list, name='my-team'),
    path('teams/create/', views.TeamCreate.as_view(), name='create-team'),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('teams/<int:pk>/update/', views.TeamUpdate.as_view(), name='team-update'),
    path('teams/<int:pk>/delete/', views.TeamDelete.as_view(), name='team-delete'),
    path('players/<int:player_id>/add/', views.add_player_to_fantasy_team, name='add-player-to-team'),
    path('players/<int:player_id>/remove/', views.remove_player_from_fantasy_team, name='remove-player-from-team'),
    path('accounts/signup/', views.signup, name='signup'),
]