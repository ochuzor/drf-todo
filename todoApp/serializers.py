from django.contrib.auth.models import User
from rest_framework import serializers
from .models import TodoItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class TodoSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = TodoItem
        fields = ['id', 'title', 'is_done', 'added_by']
