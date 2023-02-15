from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile

#Registration form
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

#Form to update user information on their profile page
class UpdateUserProfileForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'autocomplete': 'off'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}), max_length=50, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'autocomplete': 'off'}), max_length=50, required=False)

    class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', 'password1', 'password2',) #'profile_picture',)

    def __init__(self, *args, **kwargs):
        super(UpdateUserProfileForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control update-password'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['class'] = 'form-control update-password'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

        self.fields['password1'].required = False
        self.fields['password2'].required = False

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control bio-input'}), required=False)
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']