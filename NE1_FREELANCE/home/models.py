from django.db import models

# Create your models here.
class Services(models.Model):
    class Meta:
        db_table = 'home_services'
    
    title = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100, default = '')
    image = models.ImageField(upload_to='services/', blank=True, null=True)

class Jobs(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    thumbnail = models.ImageField(upload_to='services/', blank=True, null=True)