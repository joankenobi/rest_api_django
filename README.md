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
 y agregarlo en rest_api_django/settings.py en la lista de INSTALLED_APPS

## Para correr el proyecto:
```bash
python manage.py runserver
```