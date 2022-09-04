from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='users/avatars', null=True, blank=True, verbose_name='avatar')

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return f"{self.user.__str__()}'s profile"
