from django.contrib import admin
from django.utils.html import format_html
from .models import Dog, Breed


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
	list_display = ("name", "breed_group", "origin")
	search_fields = ("name", "breed_group", "origin")


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
	list_display = ("name", "breed", "age", "gender")
	search_fields = ("name", "breed__name")
