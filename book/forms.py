from django import forms
from .models import Books


class BookForms(forms.ModelForm):
    ''' Make a form Bookforms '''
    book_name = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Book Name',
                                                  'class': 'input-text'})
                )
    author = forms.CharField(
                    max_length=30,
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Author',
                                                  'class': 'input-text'})
                )
    book_id = forms.IntegerField(
                        label='',
                        widget=forms.TextInput(attrs={'placeholder': 'Book Id',
                                                      'class': 'input-text'})
                )
    no_of_book = forms.IntegerField(
                    label='',
                    widget=forms.TextInput(attrs={'placeholder': 'No of Books',
                                                  'class': 'input-text'})
                )

    class Meta:
        model = Books
        fields = '__all__'
