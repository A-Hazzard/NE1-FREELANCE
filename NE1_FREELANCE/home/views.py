from django.shortcuts import render
from .models import Services

# Create your views here.
def index(request):
    services = Services.objects.all()
    
    context = {
        'services' : services
        
        }
    return render(request, 'index.html', context)