from django.contrib import admin

# Register your models here.
from .models import Services, Jobs

admin.site.register(Services)
admin.site.register(Jobs)