from django.db import models
from datetime import datetime

class Service(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100, default = '')
    image = models.ImageField(upload_to='services/', blank=True, null=True)


    def __str__(self):
        return "Title: " + self.title

