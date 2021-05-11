from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TodoItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'created_by', 'is_done']
