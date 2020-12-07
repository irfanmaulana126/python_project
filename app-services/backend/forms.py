from django import forms
from .models import UserProfileAdmin
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileAdminForm(forms.ModelForm):
    class Meta():
         model = UserProfileAdmin
         fields = ('nama','foto_profil')