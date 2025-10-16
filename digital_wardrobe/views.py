from django.shortcuts import render, redirect
from wardrobe.models import Outfit

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index_guest.html')  # незареганные

    outfits = Outfit.objects.all().order_by('-id')[:10]  # последние 10 образов
    return render(request, 'index_user.html', {'outfits': outfits})
