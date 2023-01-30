from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError

from .models import Service
from searchResults.models import JobCategory

import datetime


# Create your views here.
def index(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()

    # search_jobs(request)
    return render(request,'home/index.html' , {'services' : services, 'job_category': job_category})
