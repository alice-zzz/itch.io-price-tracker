# itch.io-price-tracker
Receive alerts when your favourite games are within your means to purchase!

# Demo 
![alt text](https://i.ibb.co/84nWWFxB/image.png "Website Demo Image")

# Why I built this
I have recently gotten into playing cozy indie games in my free time on sites like Steam and itch.io. However, I have noticed that most games will, at some point in the year, become very dramatically on sale (up to 90% off). Since I would love to save money if possible, I decided to combine web scraping and notifications from my macOS system to alert me when a game reaches a certain target price or percent off. 
Additionally, I wanted to try web-scraping for the first time, and itch.io, where webpages have uniform html class names, was the perfect place to start. I chose itch.io rather than Steam because web scraping is against Steam's ToS.

# Features and Implementation
Daily Scrape: Every morning at 10:40 AM, the site will automatically scrape the games it is currently tracking and add it to its log.

Add Games: By pasting an itch.io game page's url and clicking "Add Game", the game will be added to the tracked games list and will be scraped daily. Whenever this game meets or exceeds the wanted price/discount, a notification will be sent. 

Scrape All Now: There is also the option of manually scraping all sites instantly. 

Price History Data: For each game, its entire price history from when it was added is stored in an SQLite3 database and can be viewed by clicking the game name on the home page.

macOS Alert: When price falls below target price or discount exceeds target discount, a macOS notification is sent announcing the game name and its current price and discount. 

# Future Improvements
Graphing and Historical Low: Each game's full price history is already being tracked for every scrape run. This could be extended further by creating a graphical showcase of the historical price data of each game. Additionally, the historical price data can be used to send an additional alert whenever a price reaches a historical low. 

Usability: Since this was just supposed to solve a small problem for myself, the ability to set a target price/discount and the ability to delete an added game are only available to admin. These features should be added to the website itself for anyone to use.
