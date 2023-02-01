from django.shortcuts import render
from django.http import HttpResponse
from searchResults.models import Job, JobCategory
from .forms import CreateJobForm

# Create your views here.
def jobForm(request):
    job_category = JobCategory.objects.all()
    
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CreateJobForm()

    return render(request, 'createjob/createjob.html', {'form': form, 'job_category': job_category})



def success(request):
    #Fetching the user data that was sent via the HTTP Request
    title = request.GET['title']
    description = request.GET['description']
    price = request.GET['price']
    category_id = request.GET['category']
    category = JobCategory.objects.get(id=category_id).name
    
    info = [ title, description, price, category ]


    for i in info:
        print("\nTitle:", title, "\nDescription:", description, "\nPrice:", price, "\nCategory:", category + "\n")
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
            print("\nData entered successful\n")
            job_category = JobCategory.objects.get(name=category)
            job = Job(title=title, description=description, price=price, category=job_category)

            if job:
                job.save()
                print('Job Created')
            else:
                print("Error creating job")
                
            return HttpResponse("<h1>SUCCESS</h1>")