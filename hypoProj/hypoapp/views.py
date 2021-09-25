from django.http import HttpResponse
from django.contrib.sites import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(('GET',))
def listPost(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)