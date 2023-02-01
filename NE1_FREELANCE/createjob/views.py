from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from searchResults.models import Job, JobCategory
from .forms import CreateJobForm

# Create your views here.
def jobForm(request):
    #Get all the job categories
    job_category = JobCategory.objects.all()
    
    #if the user sends a POST request I.E if they submit the form
    if request.method == 'POST':
        #Gather the data inputted from the form
        form = CreateJobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            # return render(request, 'createjob/createjob.html', {'error' : 'Dont leave any fields blank', 'form' : form})
            messages.success(request, "VIOLATION. Left one or more fields blank")
            return redirect('job_form')
    
    
    
    
    else:
        #if user didn't POST a request I.E user only visited the page, display the form
        form = CreateJobForm()
        return render(request, 'createjob/createjob.html', {'form': form, 'job_category': job_category})




def jobs(request):
    return HttpResponse("<h1>SUCCESS</h1>")