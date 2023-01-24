from django.shortcuts import render
from django.db.models import Q
from spellchecker import SpellChecker
from .models import Job, JobCategory

# def search_jobs(request):
#     search_term = request.GET.get('search')
#     category_name = request.GET.get('category')
#     spell = SpellChecker()
#     corrected_term = spell.correction(search_term)

#     if corrected_term != search_term:
#         did_you_mean = "Did you mean: "
#     else:
#         did_you_mean = ""

#     if category_name:
#         category = Category.objects.get(name=category_name)
#         jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term), category=category)
#     else:
#         jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
#     categories = Category.objects.all()
#     return render(request, 'searchResults/search_results.html', {'jobs': jobs, 'search_term': search_term, 'did_you_mean': did_you_mean, 'corrected_term': corrected_term, 'category': category_name, 'categories': categories})

def search_jobs(request):
    if request.method == 'POST':
        search_term = request.POST.get('search')
        category_name = request.POST.get('category')
        spell = SpellChecker()
        corrected_term = spell.correction(search_term)
        if corrected_term != search_term:
            did_you_mean = "Did you mean: "
        else:
            did_you_mean = ""
        if category_name:
            category = JobCategory.objects.filter(name=category_name).first()
            jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term), category=category)
        else:
            jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
        categories = JobCategory.objects.all()
        return render(request, 'searchResults/search_results.html', {'jobs': jobs, 'search_term': search_term, 'did_you_mean': did_you_mean, 'corrected_term': corrected_term, 'category': category_name, 'categories': categories})
    elif request.method == 'GET':
        search_term = request.GET.get('search')
        category_name = request.GET.get('category')
        spell = SpellChecker()
        corrected_term = spell.correction(search_term)
        if corrected_term != search_term:
            did_you_mean = "Did you mean: "
        else:
            did_you_mean = ""
        if category_name:
            category = JobCategory.objects.get(name=category_name)
            jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term), category=category)
        else:
            jobs = Job.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))
        categories = JobCategory.objects.all()
        return render(request, 'searchResults/search_results.html', {'jobs': jobs, 'search_term': search_term, 'did_you_mean': did_you_mean, 'corrected_term': corrected_term, 'category': category_name, 'categories': categories})
