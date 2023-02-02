from django import forms
from searchResults.models import Job, JobCategory
from django.utils.safestring import mark_safe

 
class CreateJobForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    description = forms.CharField(
        label='Description',
        max_length=255, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    price = forms.DecimalField(
        label='Price',
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=True,
    )
    category = forms.ModelChoiceField(
        label='Category',
        queryset=JobCategory.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )
  


    class Meta:
        model = Job
        fields = ['title', 'description', 'price', 'category']
