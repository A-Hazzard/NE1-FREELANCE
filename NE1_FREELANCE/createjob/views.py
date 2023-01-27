from django.shortcuts import render
from django.http import HttpResponse
from searchResults.models import Job, JobCategory
# Create your views here.
def jobForm(request):
    job_category = JobCategory.objects.all()
    
    return render(request, 'createjob/createjob.html', {'job_category': job_category})

def success(request):
    #Fetching the user data that was sent via the HTTP Request
    title = request.GET.get('title')
    description = request.GET.get('description')
    price = request.GET.get('price')
    category = request.GET.get('category')

    info = [ title, description, price, category ]


    for i in info:
        if i == '':
            print ('\nERROR! Cant leave field empty\n')
            cannot_leave_space_blank_ERROR = "Do not leave any fields empty" 
            job_category = JobCategory.objects.all()
            context = {
                "error" : cannot_leave_space_blank_ERROR,
                "job_category" : job_category
            }
            return render(request, "createjob/createjob.html", context)

        else:
            #Creating a job from the user input
            job_category = JobCategory.objects.get(name=category)
            job = Job(title=title, description=description, price=price, category=job_category)

            if job:
                job.save()
                print('Job Created')
            else:
                print("Error creating job")
                
            return HttpResponse("<h1>SUCCESS</h1>")