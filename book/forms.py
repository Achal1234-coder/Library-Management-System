from django import forms
from .models import Books


class BookForms(forms.ModelForm):
    ''' Make a form Bookforms '''
    
    class Meta:
        model = Books
        fields = '__all__'
