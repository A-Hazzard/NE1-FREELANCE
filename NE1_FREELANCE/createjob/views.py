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
        form = CreateJobForm(request.POST, request.FILES)

        print("Form data: ", form.data)
        
        if form.is_valid():
            print("Form is valid")
            form.save()
            return redirect('jobs')
        else:
            print("Form is not valid")
            messages.success(request, "Don't leave fields blank")
            return redirect('job_form')
    
    
    
    
    else:
        #if user didn't POST a request I.E user only visited the page, display the form
        form = CreateJobForm()
        return render(request, 'createjob/createjob.html', {'form': form, 'job_category': job_category})


        

def jobs(request):
    return HttpResponse("<h1>SUCCESS</h1>")