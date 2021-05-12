from django.db import models
from django.contrib.auth.models import User


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.title)
