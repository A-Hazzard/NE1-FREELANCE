from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Venue)
# admin.site.register(MyClubUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue', 'event_date')
    ordering = ('name',)
    search_fields = ('name', 'event_date')

@admin.register(MyClubUser)
class MyClubUserAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return obj.first_name + " " + obj.last_name

    list_display = ("full_name", 'email')
    ordering = ('first_name',)
    search_fields = ('first_name', "email")