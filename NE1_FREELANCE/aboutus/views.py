from django.shortcuts import render
from .models import AboutUsContent

def aboutus(request):
    information = AboutUsContent.objects.get(id=1)
    return render(request,'aboutus/aboutus.html', {'information':information})