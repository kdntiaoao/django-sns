from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.


class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    good = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    readText = models.TextField(null=True, blank=True, default='')
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
