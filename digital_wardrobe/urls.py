from django.contrib import admin
from django.urls import path, include
from wardrobe.views import index  # ✅ импортируем нашу общую главную (index)
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from wardrobe.api import ItemViewSet, OutfitViewSet

# 🔹 создаем маршруты API
router = DefaultRouter()
router.register(r'api/items', ItemViewSet)
router.register(r'api/outfits', OutfitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # ✅ главная страница (гость или пользователь)
    path('accounts/', include('users.urls')),
    path('wardrobe/', include('wardrobe.urls')),
    path("test/", include("wardrobe.urls")),

]

# 🔹 добавляем API в urlpatterns
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
