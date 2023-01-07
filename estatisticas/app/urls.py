from django.urls import path
from . import views

urrpatterns = [
    path('', views.index, name='index'),
]