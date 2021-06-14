from django import forms
from .models import RegistrationStudent


class RegisterStudentForm(forms.Form):
    ''' Make a form named RegisterStudentForm '''

    student_name = forms.CharField(max_length=30)
    student_id = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_student_name(self):
        ''' this function check the validation of student_name field '''

        name = self.cleaned_data.get('student_name')
        if len(name) < 3 or name is None:
            raise forms.ValidationError('Not valid')
        else:
            return name

    def clean_password(self):
        ''' this function check the validation of password field '''

        password = self.cleaned_data.get('password')
        if len(password) < 5:
            raise forms.ValidationError('Password to short')
        else:
            return password


class LoginStudentForm(forms.ModelForm):
    ''' Make a form named RegisterStudentForm '''
    
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    class Meta:
        model = RegistrationStudent
        fields = [
            'student_id',
            'password'
        ]
