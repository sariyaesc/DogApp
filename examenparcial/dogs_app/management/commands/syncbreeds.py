import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from dogs_app.models import Breed


class Command(BaseCommand):
    help = 'Fetch breeds from TheDogAPI and sync into local Breed model'

    def handle(self, *args, **options):
        api_key = getattr(settings, 'DOG_API_KEY', '')
        if not api_key:
            self.stdout.write(self.style.ERROR('DOG_API_KEY not set in settings or environment.'))
            return

        url = 'https://api.thedogapi.com/v1/breeds'
        headers = {'x-api-key': api_key}

        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to fetch breeds: {e}'))
            return

        data = resp.json()
        count = 0
        for item in data:
            api_id = item.get('id')
            name = item.get('name')
            breed_group = item.get('breed_group')
            origin = item.get('origin')
            temperament = item.get('temperament')
            life_span = item.get('life_span') or item.get('life_span')
            reference_image_id = item.get('reference_image_id')
            image = item.get('image') or {}
            image_url = image.get('url') if isinstance(image, dict) else None
            description = item.get('description')

            if not name:
                continue

            obj, created = Breed.objects.update_or_create(
                api_id=api_id,
                defaults={
                    'name': name,
                    'breed_group': breed_group,
                    'origin': origin,
                    'temperament': temperament,
                    'life_span': life_span,
                    'reference_image_id': reference_image_id,
                    'image_url': image_url,
                    'description': description,
                }
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f'Synced breeds. New records: {count}'))
