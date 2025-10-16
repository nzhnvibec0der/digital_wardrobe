import os
import django
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digital_wardrobe.settings')

django.setup()

# 🔥 Автоматически прогоняем миграции при старте
try:
    call_command('migrate', interactive=False)
    call_command('collectstatic', interactive=False, verbosity=0)
    print("✅ Database migrated & static collected successfully.")
except Exception as e:
    print(f"⚠️ Migration error: {e}")

application = get_wsgi_application()

import os
from django.contrib.auth.models import User

# --- Автоматическое создание суперпользователя при первом деплое ---
try:
    username = os.getenv("ADMIN_USER")
    email = os.getenv("ADMIN_EMAIL")
    password = os.getenv("ADMIN_PASSWORD")

    if username and password and not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superuser '{username}' created successfully on startup.")
except Exception as e:
    print(f"⚠️ Skipping admin auto-create: {e}")
