from django.contrib import admin
from django.urls import path, include
from game.views import game_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', game_view, {'game_id': 'default'}, name='home'),  # Root URL directs to the game
    path('game/', include('game.urls')),
]
