from django.db import models

class Game(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    target_price = models.FloatField(null=True, blank=True)
    target_discount = models.IntegerField(null=True, blank=True)  

    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PriceHistory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='prices')
    discount = models.IntegerField(null=True, blank=True)
    current_price = models.FloatField()
    original_price = models.FloatField(null=True, blank=True)
    date_checked = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_checked']

    def __str__(self):
        return f"{self.game.title} - {self.date_checked}"