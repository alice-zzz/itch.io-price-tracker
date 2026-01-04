from django.core.management.base import BaseCommand
from scraper.scraper_use import scrape_all 

class Command(BaseCommand):
    help = 'Scrape all tracked games daily'

    def handle(self, *args, **options):
        scrape_all()
        self.stdout.write(self.style.SUCCESS('Daily scrape completed!'))
