from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        """
        Clase Meta que define el modelo y los campos a serializar (convertir a Json).
        """
        fields = '__all__' # can serializer only some fields, for example: ('title', 'description')
        model = Task # model to serialize, is necessary to import the model from models.py.
        