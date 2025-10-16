from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from .models import Item, Outfit
from .forms import ItemForm, OutfitForm
from .utils import remove_background
import io


# 🧥 Мой гардероб
@login_required
def my_wardrobe(request):
    items = Item.objects.filter(user=request.user)

    # фильтры
    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    color = request.GET.get("color", "")
    season = request.GET.get("season", "")

    if search:
        items = items.filter(name__icontains=search)
    if category:
        items = items.filter(category=category)
    if color:
        items = items.filter(color=color)
    if season:
        items = items.filter(season=season)

    # динамические цвета (только те, что реально есть у пользователя)
    available_colors = (
        Item.objects.filter(user=request.user)
        .exclude(color="")
        .values_list("color", flat=True)
        .distinct()
    )

    outfits = Outfit.objects.filter(owner=request.user)
    return render(
        request,
        "wardrobe/my_wardrobe.html",
        {
            "items": items,
            "outfits": outfits,
            "search": search,
            "category": category,
            "color": color,
            "season": season,
            "available_colors": available_colors,
        },
    )



# ➕ Добавить вещь
@login_required
def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user

            image_file = request.FILES["image"]

            # читаем в отдельный объект, чтобы не потерять данные
            from django.core.files.uploadedfile import InMemoryUploadedFile
            import io

            img_copy = io.BytesIO(image_file.read())
            image_file.seek(0)  # возвращаем указатель для формы
            img_copy.seek(0)

            processed_image = remove_background(img_copy)
            processed_image.seek(0)

            item.image.save(
                f"{image_file.name.split('.')[0]}_nobg.png",
                ContentFile(processed_image.read()),
                save=True,
            )
            return redirect("my_wardrobe")
    else:
        form = ItemForm()
    return render(request, "wardrobe/add_item.html", {"form": form})


# 👗 Создать образ
@login_required
def create_outfit(request):
    from .models import Item, Outfit  # на всякий случай

    items = Item.objects.filter(user=request.user)  # ✅ показываем только вещи пользователя

    if request.method == "POST":
        name = request.POST.get("name")
        item_ids = request.POST.get("items", "").split(",")

        outfit = Outfit.objects.create(name=name, owner=request.user)
        outfit.items.set(Item.objects.filter(id__in=item_ids))
        outfit.save()

        return redirect("my_wardrobe")

    return render(request, "wardrobe/create_outfit.html", {"items": Item.objects.filter(user=request.user), "debug": "ШАБЛОН ПОДХВАЧЕН ✅"})




@login_required
def index_user(request):
    outfits = Outfit.objects.all().select_related('owner').prefetch_related('items')
    return render(request, "index_user.html", {"outfits": outfits})

from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        # Если пользователь вошёл — показываем ленту
        return redirect('index_user')
    else:
        # Если не вошёл — показываем гостевую страницу
        return render(request, 'index_guest.html')

from django.shortcuts import render
from wardrobe.views import index_user

def index(request):
    if request.user.is_authenticated:
        return index_user(request)
    return render(request, 'index_guest.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('my_wardrobe')  # перенаправление после добавления
        else:
            print(form.errors)
    else:
        form = ItemForm()
    return render(request, 'wardrobe/add_item.html', {'form': form})

# wardrobe/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Outfit
from .forms import ItemForm, OutfitForm

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('my_wardrobe')
    else:
        form = ItemForm(instance=item)
    return render(request, 'wardrobe/edit_item.html', {'form': form})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('my_wardrobe')
    return render(request, 'wardrobe/confirm_delete.html', {'object': item, 'type': 'вещь'})

@login_required
def delete_outfit(request, outfit_id):
    outfit = get_object_or_404(Outfit, id=outfit_id, owner=request.user)
    if request.method == 'POST':
        outfit.delete()
        return redirect('my_wardrobe')
    return render(request, 'wardrobe/confirm_delete.html', {'object': outfit, 'type': 'образ'})

from django.http import HttpResponse

def test_view(request):
    return HttpResponse("<h1 style='color:red;'>Тест шаблонов Django работает</h1>")

from django.shortcuts import render

def about(request):
    return render(request, "wardrobe/about.html")

def contact(request):
    return render(request, "wardrobe/contact.html")

def faq(request):
    return render(request, "wardrobe/faq.html")

def how_it_works(request):
    return render(request, "wardrobe/how_it_works.html")
