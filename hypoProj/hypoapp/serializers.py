from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['idpost', 'author', 'datepost', 'text']


"""class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('idpost', 'author', 'datepost', 'text')
"""