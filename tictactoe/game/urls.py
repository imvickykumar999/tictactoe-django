from django.urls import path
from .views import game_view, play_move, reset_game

urlpatterns = [
    path('<str:game_id>/', game_view, name='game_view'),
    path('<str:game_id>/move/<int:index>/', play_move, name='play_move'),
    path('<str:game_id>/reset/', reset_game, name='reset_game'),
]
