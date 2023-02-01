from django import forms
from searchResults.models import Job, JobCategory

class CreateJobForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)
    price = forms.DecimalField(decimal_places=2)
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all(), widget=forms.Select)
    
    class Meta:
        model = Job
        fields = ['title', 'description', 'price', 'category']
