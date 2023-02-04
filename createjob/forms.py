from django import forms
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

from searchResults.models import Job, JobCategory
from django.utils.safestring import mark_safe

 
class CreateJobForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        max_length=50, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    description = forms.CharField(
        label='Description',
        max_length=255, 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    ) 
    price = forms.DecimalField(
        label='Price',
        decimal_places=2, 
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    category = forms.ModelChoiceField(
        label='Category',
        queryset=JobCategory.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    thumbnail = forms.ImageField(
        label='Thumbnail',
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
    )


    class Meta:
        model = Job
        fields = ['title', 'description', 'price', 'category', 'thumbnail']
