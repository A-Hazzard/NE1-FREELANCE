from django.db import models

# Create your models here.
class Product(models.Model):
    title   = models.TextField(default = 'Title of the product...')
    description = models.TextField(default = 'Details about this product...')
    price = models.TextField(default = 'Cost...')
    summary = models.TextField(default='Summary of description...')

f