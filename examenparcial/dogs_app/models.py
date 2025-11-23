from django.db import models

class Breed(models.Model):
    api_id = models.IntegerField(unique=True, null=True, blank=True)
    name = models.CharField(max_length=200)
    breed_group = models.CharField(max_length=200, null=True, blank=True)
    origin = models.CharField(max_length=200, null=True, blank=True)
    temperament = models.TextField(null=True, blank=True)
    life_span = models.CharField(max_length=100, null=True, blank=True)
    reference_image_id = models.CharField(max_length=100, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Dog(models.Model):
    GENDER_CHOICES = (
        ("M", "Macho"),
        ("F", "Hembra"),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    color = models.CharField(max_length=100)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
