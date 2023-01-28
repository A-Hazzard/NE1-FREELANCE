from django.db import models

# Create your models here.
class User(models.Model):

    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class Service(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100, default = '')
    image = models.ImageField(upload_to='services/', blank=True, null=True)

