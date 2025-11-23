from django import forms
from .models import Dog


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ["name", "age", "breed", "gender", "color", "favorite_food", "favorite_toy"]