from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def jobForm(request):
    return render(request, 'createjob/createjob.html', {})

def success(request):
    return HttpResponse("<h1>SUCCESS")