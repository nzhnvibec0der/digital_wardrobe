from rest_framework import serializers, viewsets
from .models import Item, Outfit

# Сериалайзеры
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'color', 'season', 'image', 'visibility']

class OutfitSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Outfit
        fields = ['id', 'name', 'visibility', 'items']

# Вьюсеты
class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OutfitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer
