from django.shortcuts import redirect, render
from .forms import BookForms
from django.contrib import messages
from .models import Books
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url='manager:login')
def create_book_view(request):
    ''' this function work to create a new book '''

    if request.user.is_superuser:
        if request.method == 'GET':
            form = BookForms()
        else:
            form = BookForms(request.POST, request.FILES)
            print(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'New Book added successfully')
                form = BookForms()
            else:
                messages.error(request, 'not valid')

        return render(request, 'book/create.html', {'form': form})

    else:

        return HttpResponse('<h1> You are not authorized for this page</h1>')


@login_required(login_url='start:home')
def read_book_view(request):
    ''' this function work to read all books and return '''

    book_obj = Books.objects.all()
    return render(request, 'book/read.html', {'book_obj': book_obj})


@login_required(login_url='manager:login')
def update_book_view(request, book_id):
    ''' this function work to udate a book'''

    if request.user.is_superuser:

        try:
            book_obj = Books.objects.get(id=book_id)
        except ObjectDoesNotExist:
            messages.error(request, 'Book does not exist in database')
            return redirect('book:read')

        form = BookForms(instance=book_obj)

        if request.method == 'POST':
            form = BookForms(request.POST, instance=book_obj)
            if form.is_valid():
                form.save()
                return redirect('book:read')

        return render(request, 'book/create.html', {'form': form})

    else:

        return HttpResponse('<h1> You are not authorized for this page</h1>')


@login_required(login_url='manager:login')
def delete_book_view(request, book_id):
    ''' this function work to delete a book '''

    if request.user.is_superuser:

        try:
            book_obj = Books.objects.get(id=book_id)
        except ObjectDoesNotExist:
            messages.error(request, 'Book does not exist in database')
            return redirect('book:read')

        book_obj.delete()

        return redirect('book:read')

    else:

        return HttpResponse('<h1> You are not authorized for this page</h1>')


@login_required(login_url='start:home')
def search_view(request):
    ''' this function search a specific book and render it '''
    
    book = request.GET.get('book_search')
    book_obj = Books.objects.filter(book_name=book)
    return render(request, 'book/read.html', {'book_obj': book_obj})
