from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterStudentForm(UserCreationForm):
    ''' Make a register form named RegisterStudentForm '''

    username = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                  'class': 'input-text'})
                )
    email = forms.EmailField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                  'class': 'input-text'})
                )
    password1 = forms.CharField(
                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                  'class': 'input-text'}),
                label=''
            )
    password2 = forms.CharField(

            widget=forms.PasswordInput(attrs={'placeholder': 'ConfirmPassword',
                                              'class': 'input-text'}),
            label=''
            )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class LoginStudentForm(forms.Form):
    ''' Make a login form named LoginStudentForm '''

    student_name = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                  'class': 'input-text'})
                )
    password = forms.CharField(
                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                  'class': 'input-text'}),
                label=''
            )
