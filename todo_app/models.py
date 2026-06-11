from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    completion = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)