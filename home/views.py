from django.shortcuts import render, redirect

from .models import Service
from searchResults.models import JobCategory


# Create your views here.
def index(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()

    if request.user.is_authenticated: #if they are logged in
        return redirect("search_jobs")
    else:
        # search_jobs(request)
        return render(request,'home/index.html' , {'services' : services, 'job_category': job_category})
