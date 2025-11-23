from django.urls import path
from .views import DogCreateView, DogListView, DogImageView
from .views import BreedInfoView


urlpatterns = [
    path("dogs/add/", DogCreateView.as_view(), name="dog_create"),
    path("dogs/", DogListView.as_view(), name="dog_list"),
    path("dogs/random-image/", DogImageView.as_view(), name="random_dog"),
    path("dogs/breed/<int:pk>/", BreedInfoView.as_view(), name="breed_info"),
]