from django.db import models

class JobCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title






# from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=255)

# class Job(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

# class JobCategory(models.Model):
#     category = models.CharField(max_length=255)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         Job.objects.filter(category=None).update(category=self)
