from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('shirt', 'Футболка'),
        ('jacket', 'Куртка'),
        ('pants', 'Брюки'),
        ('shoes', 'Обувь'),
        ('accessory', 'Аксессуар'),
    ]
    SEASON_CHOICES = [
        ('summer', 'Лето'),
        ('autumn', 'Осень'),
        ('winter', 'Зима'),
        ('spring', 'Весна'),
    ]
    VISIBILITY_CHOICES = [
        ('private', 'Только я'),
        ('public', 'Видно всем'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=30, blank=True)
    season = models.CharField(max_length=20, choices=SEASON_CHOICES)
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')

    def __str__(self):
        return f"{self.name} ({self.user.username})"

visibility = models.CharField(
    max_length=10,
    choices=[('private', 'Только я'), ('public', 'Видно всем')],
    default='private'
)


class Outfit(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'Только я'),
        ('public', 'Видно всем'),
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outfits')
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='outfits')
    created_at = models.DateTimeField(auto_now_add=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')


    def __str__(self):
        return f"Образ: {self.name} ({self.owner.username})"
