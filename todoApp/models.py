from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
