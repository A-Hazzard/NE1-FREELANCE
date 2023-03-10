from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class AboutUsContent(models.Model):
    information = RichTextField(config_name='default') ##text formatter for textarea fields. pip install django-ckeditor


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='info/')

    