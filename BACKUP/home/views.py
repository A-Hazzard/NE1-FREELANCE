from django.shortcuts import render
from .models import Service
from searchResults.models import JobCategory
# from searchResults.views import search_jobs

# Create your views here.
def index(request):
    services = Service.objects.all()
    job_category = JobCategory.objects.all()

    # search_jobs(request)
    return render(request,'home/index.html' , {'services' : services, 'job_category': job_category})