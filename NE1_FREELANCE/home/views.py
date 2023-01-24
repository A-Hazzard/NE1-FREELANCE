from django.shortcuts import render
from .models import Services

# Create your views here.
def index(request):
    services = Services.objects.all()
    
    return render(request,'home/index.html' , {'services' : services})