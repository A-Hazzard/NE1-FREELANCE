from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from createjob import views as create_job
from .views import jobForm, success

urlpatterns = [
    path('', jobForm, name = "job_form"),
    path('created=True/', success, name = 'create_job'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
