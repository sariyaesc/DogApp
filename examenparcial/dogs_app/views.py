from django.shortcuts import render, redirect
from django.views import View
from .forms import DogForm
from .models import Dog, Breed
import requests
from django.conf import settings
from django.http import JsonResponse, Http404


# ---------------------------
# Vista para crear perros
# ---------------------------
class DogCreateView(View):
    def get(self, request):
        form = DogForm()
        return render(request, "dog_form.html", {"form": form})


    def post(self, request):
        form = DogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dog_list") # Redirecciona al listado
        return render(request, "dog_form.html", {"form": form})


# ---------------------------
# Listar perros
# ---------------------------
class DogListView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        return render(request, "dog_list.html", {"dogs": dogs})


# ---------------------------
# API externa (TheDogAPI)
# ---------------------------
def get_random_dog_image():
    url = "https://api.thedogapi.com/v1/images/search"
    headers = {"x-api-key": settings.DOG_API_KEY}
    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        data = response.json()
        return data[0]["url"]
    return None


class DogImageView(View):
    def get(self, request):
        image_url = get_random_dog_image()
        return render(request, "random_dog_image.html", {"image_url": image_url})


class BreedInfoView(View):
    def get(self, request, pk):
        try:
            breed = Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404("Breed not found")

        data = {
            'id': breed.id,
            'api_id': breed.api_id,
            'name': breed.name,
            'breed_group': breed.breed_group,
            'origin': breed.origin,
            'temperament': breed.temperament,
            'life_span': breed.life_span,
            'image_url': breed.image_url,
            'description': breed.description,
        }
        return JsonResponse(data)