from django.contrib import admin
from .models import Game, PriceHistory

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'added_date', 'target_price', 'target_discount']
    search_fields = ['title', 'url']

@admin.register(PriceHistory)
class PriceHistoryAdmin(admin.ModelAdmin):
    list_display = ['game', 'current_price', 'original_price', 'discount', 'date_checked']
    list_filter = ['date_checked']

