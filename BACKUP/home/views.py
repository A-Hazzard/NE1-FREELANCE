from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    
    return render(request,'home/index.html' , {'services' : services})