from django import forms
from searchResults.models import Job, JobCategory
class CreateJobForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    description = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    price = forms.DecimalField(decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    category = forms.ModelChoiceField(queryset=JobCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=True)
    
    class Meta:
        model = Job
        fields = ['title', 'description', 'price', 'category']
