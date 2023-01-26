from django.db import models

# Create your models here.
class AboutUsContent(models.Model):
    information = models.TextField(max_length=1000)