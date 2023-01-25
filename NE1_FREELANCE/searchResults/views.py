from django.shortcuts import render
from django.db.models import Q
from .models import Job, JobCategory
import fuzzywuzzy
from fuzzywuzzy import process

def search_jobs(request):
    search_term = request.GET.get('search')
    if search_term is None:
        search_term = ''
    category_name = request.GET.get('category')
    category = None
    if category_name:
        category = JobCategory.objects.filter(name__iexact=category_name).first()

    jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
    if category:
        jobs = jobs.filter(category=category)

    did_you_mean = None
    corrected_term = None
    if not jobs:
        title_matches = process.extract(search_term, [job.title for job in Job.objects.all()], limit=1, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
        if title_matches:
            did_you_mean = "Did you mean?"
            corrected_term = title_matches[0][0]
    else:
        corrected_term = search_term
    
    categories = JobCategory.objects.all()
    context = {
        'jobs': jobs,
        'search_term': search_term,
        'did_you_mean': did_you_mean,
        'corrected_term': corrected_term,
        'categories': categories,
        'category_name': category_name
    }
    return render(request, 'searchResults/search_results.html', context)






# def search_jobs(request):
#     search_term = request.GET.get('search')
#     if not search_term:
#         search_term = request.POST.get('search')
#     category_name = request.GET.get('category')
#     category = None
#     if category_name:
#         category = JobCategory.objects.filter(name__iexact=category_name).first()

#     jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
#     if category:
#         jobs = jobs.filter(category=category)

#     did_you_mean = None
#     corrected_term = None
#     if not jobs:
#         title_matches = get_close_matches(search_term, [job.title for job in Job.objects.all()], n=1, cutoff=0.7)
#         if title_matches:
#             did_you_mean = "Did you mean?"
#             corrected_term = title_matches[0]
#     else:
#         corrected_term = search_term
    
#     categories = JobCategory.objects.all()
#     context = {
#         'jobs': jobs,
#         'search_term': search_term,
#         'did_you_mean': did_you_mean,
#         'corrected_term': corrected_term,
#         'categories': categories,
#         'category_name': category_name,
#     }
#     return render(request, 'searchResults/search_results.html', context)



