from django import forms
from django.contrib.auth.models import User
from .models import Contact

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ('username','email','password',)
#
#
#
# class UserProfileInfoForm(forms.ModelForm):
#     class Meta():
#         model = UserProfileInfo
#         fields = '__all__'

class contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']