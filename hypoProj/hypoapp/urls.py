from django.urls import path, include
from . import views

urlpatterns = [
    path('listPost/', views.listPost, name='listPost'),
    ]