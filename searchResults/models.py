from django.db import models
from django.contrib.auth.models import User

class JobCategory(models.Model):
    #name of the category
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " $" + str(self.price)
