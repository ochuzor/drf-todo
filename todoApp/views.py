from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions, filters

from todoApp import serializers
from todoApp.serializers import UserSerializer, TodoSerializer
from todoApp.models import TodoItem
from todoApp.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['is_done', 'created_at']
    ordering = ['created_at']

    def get_queryset(self):
        """
        user only gets her/his own todos
        """
        return TodoItem.objects.filter(added_by=self.request.user)

    def perform_create(self, serializer):
        """
        automatically set this field before saving
        """
        serializer.save(added_by=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = serializers.TodoSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
