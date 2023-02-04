from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# models.py
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default = "profile_photos/default.png", upload_to='profile_photos', blank=True, null=True)

    def __str__(self):
            return f'{self.user.username} Profile'