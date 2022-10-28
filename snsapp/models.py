from datetime import datetime
from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.


class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to="")
    good = models.IntegerField()
    read = models.IntegerField()
    readText = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
