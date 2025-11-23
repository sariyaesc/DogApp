# DogApp

**Qué API externa elegiste**

 - **API**: `TheDogAPI` (https://thedogapi.com)
 - **Endpoints usados**: `/v1/breeds` (sincronizar razas) y `/v1/images/search` (imagen aleatoria)

**Cómo la consumiste**

 - **Comando de gestión**: `examenparcial/dogs_app/management/commands/syncbreeds.py` usa la librería `requests` para hacer `GET https://api.thedogapi.com/v1/breeds` con la cabecera `x-api-key` y sincroniza los objetos `Breed` en la base de datos (usa `Breed.objects.update_or_create`). Ejecutar:

```
python manage.py syncbreeds
```

 - **Vista para imagen aleatoria**: `examenparcial/dogs_app/views.py` define `get_random_dog_image()` que hace `GET https://api.thedogapi.com/v1/images/search` con la cabecera `x-api-key` y devuelve la URL de la primera imagen (`data[0]['url']`). La vista `DogImageView` renderiza la plantilla `random_dog_image.html` con esa URL.

 - **Configuración**: la clave de API se lee desde `DOG_API_KEY` en `examenparcial/examenparcial/settings.py` (por defecto desde la variable de entorno). Asegúrate de exportar `DOG_API_KEY` antes de ejecutar el comando o iniciar el servidor.

**Ejemplo de JSON original**

Ejemplo (respuesta típica del endpoint `GET https://api.thedogapi.com/v1/breeds` — un elemento del array):

```
{
	"weight": {"imperial":"6 - 13","metric":"3 - 6"},
	"height": {"imperial":"9 - 11.5","metric":"23 - 29"},
	"id": 1,
	"name": "Affenpinscher",
	"breed_group": "Toy",
	"life_span": "10 - 12 years",
	"temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
	"origin": "Germany, France",
	"reference_image_id": "BJa4kxc4X",
	"image": {"id":"BJa4kxc4X","width":1600,"height":1199,"url":"https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg"},
	"description": "Small, compact, and charming. The Affenpinscher is a lively companion."
}
```

**Ejemplo de JSON que tú regresas**

La vista `BreedInfoView` en `examenparcial/dogs_app/views.py` devuelve un JSON con los campos seleccionados del modelo `Breed`. Ejemplo (para el mismo elemento sincronizado):

```
{
	"id": 12,
	"api_id": 1,
	"name": "Affenpinscher",
	"breed_group": "Toy",
	"origin": "Germany, France",
	"temperament": "Stubborn, Curious, Playful, Adventurous, Active, Fun-loving",
	"life_span": "10 - 12 years",
	"image_url": "https://cdn2.thedogapi.com/images/BJa4kxc4X.jpg",
	"description": "Small, compact, and charming. The Affenpinscher is a lively companion."
}
```

**Notas rápidas**

 - **Ruta del comando**: `examenparcial/dogs_app/management/commands/syncbreeds.py`
 - **Ruta de las vistas**: `examenparcial/dogs_app/views.py`
 - **Key en settings**: `DOG_API_KEY` (establecer en entorno antes de usar)

Si quieres, puedo: añadir un ejemplo de `.env` y un pequeño script de ayuda, o generar pruebas unitarias para la sincronización. ¿Cuál prefieres?