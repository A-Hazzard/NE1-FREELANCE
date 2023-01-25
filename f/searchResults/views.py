from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Job, JobCategory
from difflib import get_close_matches

def search_jobs(request):
    search_term = request.GET.get('search')
    category_name = request.GET.get('category')
    category = None
    if category_name:
        category = JobCategory.objects.get(name=category_name)
    jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
    if category:
        jobs = jobs.filter(category=category)

    did_you_mean = None
    corrected_term = None
    if not jobs:
        title_match = get_close_matches(search_term, [job.title for job in Job.objects.all()])
        if title_match:
            did_you_mean = "Did you mean?"
            corrected_term = title_match[0]

    categories = JobCategory.objects.all()
    context = {
        'jobs': jobs,
        'search_term': search_term,
        'did_you_mean': did_you_mean,
        'corrected_term': corrected_term,
        'categories': categories,
        'category_name': category_name,
    }
    return render(request, 'searchResults/search_results.html', context)
