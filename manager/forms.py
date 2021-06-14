from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ManagerRegistrationForm(UserCreationForm):
    admin_password = forms.CharField(widget=forms.PasswordInput())
    manager_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['admin_password', 'manager_name']


class ManagerLoginForm(forms.Form):
    book_manager_name = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
