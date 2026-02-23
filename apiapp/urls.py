from django.urls import path
from .views import PrivateHello

urlpatterns = [
    path("private/", PrivateHello.as_view()),
]