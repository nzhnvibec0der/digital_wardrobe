from django import forms
from .models import Item, Outfit

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'color', 'season', 'image', 'visibility']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Название вещи'}),
            'color': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Цвет'}),
            'category': forms.Select(attrs={'class': 'input-field'}),
            'season': forms.Select(attrs={'class': 'input-field'}),
            'image': forms.ClearableFileInput(attrs={'class': 'input-field'}),
            'visibility': forms.Select(attrs={'class': 'form-select'}),
        }



class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'items', 'visibility']
        widgets = {
            'items': forms.CheckboxSelectMultiple,
            'visibility': forms.Select(attrs={'class': 'form-select'}),
        }
