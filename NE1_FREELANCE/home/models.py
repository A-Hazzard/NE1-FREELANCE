from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100, default = '')
    image = models.ImageField(upload_to='services/', blank=True, null=True)