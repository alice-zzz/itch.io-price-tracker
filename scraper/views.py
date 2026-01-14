from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .scraper_use import add_game_with_scraping, scrape_all 

def home(request):
    games = Game.objects.prefetch_related('prices').order_by('title')
    return render(request, 'scraper/home.html', {'games': games})

def add_game(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            add_game_with_scraping(url)
    return redirect('home')

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

def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        target_price = request.POST.get('target_price')
        target_discount = request.POST.get('target_discount')

        game.target_price = float(target_price) if target_price else None
        game.target_discount = int(target_discount) if target_discount else None
        game.notified = False  # Reset notification flag
        game.save()

        return redirect('game_detail', pk=game.pk)
    
    return render(request, 'scraper/edit_game.html', {'game': game})

def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)

    if request.method == 'POST':
        game.delete()
        return redirect('home')
    
    return render(request, 'scraper/delete_game.html', {'game': game})