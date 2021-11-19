

from os import name
from django.urls import path
from .views import (
    index,
    about,
    health_benefits
)

app_name = "mainapp"
urlpatterns = [
    path('',index,name="index"),
    path('about/',about,name="about"),
    path('health/benefits/',health_benefits,name="health")
]
