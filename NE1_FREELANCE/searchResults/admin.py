from django.contrib import admin
from .models import Job, JobCategory

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'category__name')

admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory)