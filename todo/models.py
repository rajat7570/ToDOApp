from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    user = models.CharField(max_length=10)
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200)