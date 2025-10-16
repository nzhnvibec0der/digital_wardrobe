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
