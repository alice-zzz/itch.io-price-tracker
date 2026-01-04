from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/<int:pk>/', views.game_detail, name='game_detail'),
    path('scrape-all/', views.scrape_all_now, name='scrape_all_now'),
    
]
