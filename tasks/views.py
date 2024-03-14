from rest_framework import viewsets
from .models import Task
from .serializer import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet que define las acciones de la API.
    """
    queryset = Task.objects.all() # queryset to get all the objects from the model.
    serializer_class = TaskSerializer # serializer class to use in the API.
