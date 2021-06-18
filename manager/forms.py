from django import forms
from .models import IssueBook


class ManagerLoginForm(forms.Form):
    ''' Make a form to ManagerLogin'''

    manager_name = forms.CharField(
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


class IssueBookForm(forms.ModelForm):
    ''' Make a form to Issue a book '''

    student_name = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'StudentName',
                                                  'class': 'input-text'})
    )
    book_name = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Book Name',
                                                  'class': 'input-text'})
    )
    book_id = forms.IntegerField(
                label='',
                widget=forms.TextInput(attrs={'placeholder': 'Book Id',
                                              'class': 'input-text'})
    )

    class Meta:
        model = IssueBook
        fields = '__all__'
