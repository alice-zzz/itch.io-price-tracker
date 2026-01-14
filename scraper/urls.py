from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('scrape-all/', views.scrape_all_now, name='scrape_all_now'),
    path('add-game/', views.add_game, name='add_game'),
    path('games/<int:pk>/edit/', views.edit_game, name='edit_game'), 
    path('games/<int:pk>/delete/', views.delete_game, name='delete_game'),
]
