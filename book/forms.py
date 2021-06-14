from django import forms
from .models import Books


class Book_forms(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
