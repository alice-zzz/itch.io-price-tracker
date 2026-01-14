from bs4 import BeautifulSoup
import requests
import re
import subprocess
from .models import Game, PriceHistory
from datetime import datetime

def send_mac_notification(title, message):
    subprocess.run([
        'osascript', '-e',
        f'display notification "{message}" with title "{title}" sound name "default"'
    ])


#Convert scraped prices / discounts to numbers
def price_real(text):
    if text in (None, "N/A", ""):
        return None
    else:
        clean = re.sub(r"[^\d.]", "", text)
        return float(clean)
def percent_int(text): 
    if text in (None, "N/A", ""):
        return None
    else:
        clean = re.sub(r"[^\d]", "", text)
        return int(clean)


def scrape(url):
    page_to_scrape = requests.get(url)
    soup = BeautifulSoup(page_to_scrape.content, 'html.parser')

    game_title = soup.find("h1", attrs={"class": "game_title"})
    discount = soup.find("span", attrs={"class": "sale_rate"})
    current_price = soup.find("span", attrs={"itemprop": "price", "class": "dollars"})
    original_price = soup.find("span", attrs={"class": "original_price"})

    title_txt = game_title.text.strip() if game_title else "NO TITLE FOUND"
    discount_txt = discount.text.strip() if discount else "N/A"
    current_txt = current_price.text.strip() if current_price else "$0"
    original_txt = original_price.text.strip() if original_price else "$0"

    return {
        "title": title_txt,
        "discount": percent_int(discount_txt),
        "current_price": price_real(current_txt),
        "original_price": price_real(original_txt)
    }


def add_game_with_scraping(url):
    game_data = scrape(url)
    
    game, created = Game.objects.get_or_create(
        url=url,
        defaults={'title': game_data['title']}
    )
    
    price=PriceHistory.objects.create(
        game=game,
        discount=game_data['discount'],
        current_price=game_data['current_price'],
        original_price=game_data['original_price']
    )

    triggered = False
    # Target price met
    if game.target_price is not None and price.current_price is not None:
        if price.current_price <= game.target_price:
            triggered = True
    
    #  Target discount met
    if game.target_discount is not None and price.discount is not None:
        if price.discount >= game.target_discount:
            triggered = True

    # Send notification 
    if triggered and not game.notified:
        msg = f"{game.title} - Price: ${price.current_price:.2f}"
        if price.discount:
            msg += f", {price.discount}% off"
        
        print(f"PRICE ALERT!! {msg}")
        
        send_mac_notification("Itch.io Price Alert!!", msg)
        
        game.notified = True
        game.save()
    
    # Reset notification 
    if game.notified:
        if (game.target_price and price.current_price > game.target_price) or \
           (game.target_discount and (price.discount is None or price.discount < game.target_discount)):
            game.notified = False
            game.save()
            print(f"Reset notification for {game.title}")
    
    return game, created


def scrape_all():
    games = Game.objects.all()
    if not games:
        print("No games to scrape.")
        return

    for game in games:
        try:
            add_game_with_scraping(game.url)
            print(f"Scraped {game.title}")
        except Exception as e:
            print(f"Error scraping {game.title}: {e}")
