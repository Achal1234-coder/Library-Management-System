from django import forms
from .models import Registration_Student


class Register_student_form(forms.Form):
    Student_Name = forms.CharField(max_length=30)
    Student_Id = forms.IntegerField()
    Password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())

    def clean_Student_Name(self):
        name = self.cleaned_data.get('Student_Name')
        if len(name) < 3 or name is None:
            raise forms.ValidationError('Not valid')
        else:
            return name

    def clean_Password(self):
        password1 = self.cleaned_data.get('Password')
        if len(password1) < 5:
            raise forms.ValidationError('Password to short')
        else:
            return password1


class Login_student_form(forms.ModelForm):
    Password = forms.CharField(max_length=20, widget=forms.PasswordInput())

    class Meta:
        model = Registration_Student
        fields = [
            'Student_Id',
            'Password'
        ]
