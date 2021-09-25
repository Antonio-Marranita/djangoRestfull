from django.urls import path, include
from . import views

urlpatterns = [
    path('listPosts/', views.listPosts, name='listPosts'),
    path('addPost/', views.addPost, name='addPost'),
    path('viewPost/<str:pk>/', views.viewPost, name='viewPost'),
    path('deletePost/<str:pk>/', views.deletePost, name='deletePost'),
    path('updatePost/<str:pk>/', views.updatePost, name='updatePost'),
    ]
