from django.shortcuts import render
from .models import Services

# Create your views here.
def index(request):
    services = Services.objects.all()
    template = 'index.html'   
    return render(request,template, {'services' : services})