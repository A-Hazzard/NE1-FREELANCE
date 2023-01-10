from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs, ' these are the arguments returned from request')

    return render(request, "index.html", {})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(args, kwargs, ' these are the arguments returned from request')

    #return HttpResponse("<h1>Contact page</h2>")    
