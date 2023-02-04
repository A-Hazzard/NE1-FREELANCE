from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from searchResults.models import Job, JobCategory
from .forms import CreateJobForm


# Create your views here.
def jobForm(request):
    # Get all the job categories
    job_category = JobCategory.objects.all()
    print('\nPath:', request.build_absolute_uri , "\n")       

    # if the user sends a POST request I.E if they submit the form
    if request.method == 'POST':
        # Gather the data inputted from the form
        form = CreateJobForm(request.POST, request.FILES)
     

        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            print('\n', request.user, " created a job")
            return redirect('job_form')
        else:
            print('\n', request.user, " failed to create a job")
            messages.error(request, "Please fill in all the fields correctly")
            return redirect('job_form')

    # if user didn't POST a request I.E user only visited the page, display the form
    else:
        form = CreateJobForm()
        return render(request, 'createjob/createjob.html', {'form': form, 'job_category': job_category})


        

def jobs(request):
    return HttpResponse("<h1>SUCCESS</h1>")