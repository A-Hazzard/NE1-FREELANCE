from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=50)
    # profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2',) #'profile_picture',)

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['profile_picture'].widget.attrs['class'] = 'form-control'
 

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']