from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_user, name='index_user'),
    path('guest/', views.index, name='index_guest'),
    path('add/', views.add_item, name='add_item'),
    path('my/', views.my_wardrobe, name='my_wardrobe'),
    path('outfit/', views.create_outfit, name='create_outfit'),
    path('wardrobe/', views.my_wardrobe, name='my_wardrobe'),
    path("test/", views.test_view),
    path('wardrobe/', views.my_wardrobe, name='my_wardrobe'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    
    path('item/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('item/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('outfit/<int:outfit_id>/delete/', views.delete_outfit, name='delete_outfit'),
    path("test_view/", views.test_view, name="test_view"),

]

from rest_framework.routers import DefaultRouter
from .api import ItemViewSet, OutfitViewSet

router = DefaultRouter()
router.register(r'api/items', ItemViewSet)
router.register(r'api/outfits', OutfitViewSet)

urlpatterns += router.urls
