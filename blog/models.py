from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    notes = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.notes


