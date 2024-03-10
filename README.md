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
