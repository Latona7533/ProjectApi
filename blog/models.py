from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=50)
    text = models.CharField(max_length=200)
