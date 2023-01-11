from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'featured'
        ]

class RawProductForm(forms.Form):
    title   = forms.CharField(required = True, widget=forms.TextInput(attrs={"placeholder": "Title..."}))
    description = forms.CharField(required = True, widget = forms.TextInput(attrs={"placeholder":"Summary of the product..."}) )
    price   = forms.DecimalField(required = True, widget = forms.NumberInput(attrs={"placeholder":"TTD"}))