from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Manager_Registration_form(UserCreationForm):
    Admin_Password = forms.CharField(widget=forms.PasswordInput())
    Manager_Name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['Admin_Password', 'Manager_Name']


class Manager_login_form(forms.Form):
    Book_Manager_Name = forms.CharField(max_length=30)
    Password = forms.CharField(widget=forms.PasswordInput())
