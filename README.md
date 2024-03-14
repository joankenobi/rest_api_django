# rest_api_django
rest api with django

## Pasos para crear una rest api django:

1. Crear un entorno virtual:
```bash
python3 -m venv env
```

2. Activar el entorno virtual:
```bash
source env/bin/activate
```
EN WINDOWS:
```bash
venv\Scripts\activate
```

3. Instalar django:
```bash
pip install django
```
4. Crear un proyecto de django:
```bash
django-admin startproject myproject
```

Para crear el proyecto en el directorio actual:
```bash
django-admin startproject myproject .
```
5. Crear una app:
```bash
python manage.py startapp myapp
```
 y agregarlo "myapp" en rest_api_django/settings.py en la lista de INSTALLED_APPS en este caso se agregó "tasks". 

## Para correr el proyecto:
```bash
python manage.py runserver
```

6. instalar djangorestframework:
```bash
pip install djangorestframework
```

    Agregar "rest_framework" en rest_api_django/settings.py en la lista de INSTALLED_APPS

7. instalar modulo adicional que comunica backend con frontend:

    Los navegadore no permiten conectar servidores locales (de desarrollo) por seguridad, por lo que se debe instalar un modulo adicional para poder hacerlo.

```bash
pip install django-cors-headers
```
Este modulo agrega los headers que son strings que indican quien puede conectarse a nuestro backend.

    Agregar "corsheaders" en rest_api_django/settings.py en la lista de INSTALLED_APPS

    Agregar "corsheaders" en rest_api_django/settings.py en la lista de MIDDLEWARE para mostrar las respuestar y debe ir antes de CommonMiddleware 'django.middleware.common.CommonMiddleware'

8. agregar configuración de corsheaders en rest_api_django/settings.py:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000"
]
```
lista blanca de los dominios que pueden conectarse a nuestro backend.

## Modelado de tabla para guardar los datos:

Django tiene su propio ORM (Object Relational Mapping) que permite modelar las tablas de la base de datos como clases de python.

1. Crear un modelo en myapp/models.py:

```python

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
``` 
    para que django sepa que hay un nuevo modelo se debe correr el siguiente comando:
```bash
 python manage.py makemigrations
```

    en caso de solo ejecutar las migraciones de la app:
```bash
 python manage.py makemigrations myapp
``` 

2. Aplicar las migraciones:
```bash
 python manage.py migrate
``` 
con esto ya fue ejecutado el codigo en la carpeta migration y se creó la tabla en la base de datos.


## CREAR UN USUARIO ADMINISTRADOR:

1. Crear un superusuario:
```bash
 python manage.py createsuperuser (nameuser)
``` 
    y seguir las instrucciones.

para probar la api se puede ir a la url http://localhost:8000/admin y loguearse con el usuario creado.

2. Para poder ver la tabla creada en la base de datos se debe registrar el modelo en myapp/admin.py:

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

## CREAR UN SERIALIZADOR

Para este paso ya se tiene un modelo para la app que permite manipular datos desde el panel administrador, pero para poder manipular los datos desde la api se debe crear un serializador.

Dentro de la myapp se debe crear un archivo serializers.py:

```python
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
```
El serializador es para indicar que datos van a ser enviados desde el backend y pueden ser convertidos a json.

Django convierte los datos de la base de datos en objetos de python y el serializador los convierte en json.

## CREAR UNA VISTA

Django tiene vistas basadas en clases y vistas basadas en funciones.

Las vistas son funciones que responden algo al cliente.

1. Crear una vista basada en clases en myapp/views.py:

```python
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
```
    El viewset es una vista que permite hacer operaciones CRUD (Create, Read, Update, Delete) en la base de datos.

2. Crear una url para la vista en myapp/urls.py:
    
    ```python
    from django.urls import path, include

    from rest_framework.routers import DefaultRouter
    from .views import TaskViewSet

    router = DefaultRouter()
    router.register(r'tasks', TaskViewSet)

    urlpatterns = [
        path('', include(router.urls))
    ]
    ```
    El router es un objeto que permite crear urls para las vistas basadas en clases.

