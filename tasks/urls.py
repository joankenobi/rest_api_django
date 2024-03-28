from django.urls import path, include
from rest_framework import routers
from tasks.views import TaskViewSet

# generate all the urls for the API (GET, POST, PUT, DELETE) in tasks model

router = routers.DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path("api/v1/" , include(router.urls)),
    path('docs/', include_docs_urls(title='Tasks API'))
]

