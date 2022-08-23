from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

