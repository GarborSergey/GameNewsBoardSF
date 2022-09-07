from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PostCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=225)
    category = models.ManyToManyField(PostCategory, related_name='category_of_post')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_of_post')
    liked = models.ManyToManyField(User, related_name='users_liked_post', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('NewsBoard:post-detail', args=[str(self.id)])


class Message(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_user')
    date_added = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)



