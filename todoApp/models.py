from django.db import models
from django.core.validators import MinLengthValidator

class TodoItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    added_by = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
