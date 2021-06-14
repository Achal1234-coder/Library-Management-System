from django.shortcuts import render
from .forms import Book_forms
from django.contrib import messages
from .models import Books


def create_book_view(request):
    form = Book_forms(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'New Book added successfully')
        form = Book_forms()
    return render(request, 'book/create.html', {'form': form})


def read_book_view(request):
    Book_obj = Books.objects.all()
    return render(request, 'book/read.html', {'Book_obj': Book_obj})
