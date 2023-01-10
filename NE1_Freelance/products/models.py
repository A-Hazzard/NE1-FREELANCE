from django.db import models

# Create your models here.
class Product(models.Model):
    title   = models.CharField(blank = False, null = False, max_length = 50)
    description = models.TextField(blank = False, null = False)

    price = models.DecimalField(blank = False, null = False, decimal_places=2, max_digits=10000)

    summary = models.TextField(blank = False, null = False, max_length= 120)

    featured = models.BooleanField(blank = False, null = False)

