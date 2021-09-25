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

@api_view(['GET'])
def listPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewPost(request, pk):
    post = Post.objects.get(idpost=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def addPost(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(idpost=pk)
    serializer = PostSerializer(post)
    post.active = False
    post.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePost(request, pk):
    post = Post.objects.get(idpost=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)