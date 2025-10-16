from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("my_wardrobe")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        email = (request.POST.get("email") or "").strip().lower()
        password = request.POST.get("password") or ""

        if not username or not email or not password:
            messages.error(request, "Заполните все поля.")
            return render(request, "users/login.html")

        # Ищем пользователя по НИКУ
        try:
            user_obj = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Неверные данные входа.")
            return render(request, "users/login.html")

        # Проверяем соответствие email (безопасно, т.к. у User e-mail по умолчанию case-insensitive не уникален)
        if (user_obj.email or "").lower() != email:
            messages.error(request, "Неверные данные входа.")
            return render(request, "users/login.html")

        # Проверяем пароль
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Неверные данные входа.")
            return render(request, "users/login.html")

        login(request, user)
        return redirect("index_user")

    return render(request, "users/login.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("index_guest")  # или на главную, где гости видят лендинг
