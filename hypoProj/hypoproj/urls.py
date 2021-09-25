from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from hypoapp import views


router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('', include('hypoapp.urls')),
    path('admin/', admin.site.urls),
]


