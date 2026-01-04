from django.shortcuts import render, redirect
from .models import Game
from .scraper_use import add_game_with_scraping, scrape_all 

def home(request):
    if request.method == 'POST' and 'url' in request.POST:
        url = request.POST.get('url')
        if url:
            add_game_with_scraping(url)  
            return redirect('home')

    games = Game.objects.prefetch_related('prices').order_by('title')
    return render(request, 'scraper/home.html', {'games': games})

def scrape_all_now(request):
    scrape_all()
    return redirect('home')

def game_detail(request, pk):
    game = Game.objects.get(pk=pk)
    prices = game.prices.all()
    return render(request, 'scraper/game_detail.html', {
        'game': game,
        'prices': prices
    })
