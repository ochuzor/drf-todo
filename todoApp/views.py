from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from todoApp.serializers import UserSerializer, TodoSerializer
from todoApp.models import TodoItem


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
