from django.shortcuts import render, redirect
from .forms import RegisterStudentForm, LoginStudentForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from manager.models import IssueBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from book.models import Books


def home_view(request):
    ''' this method render the home.html '''

    if request.user.is_authenticated:

        if request.user.is_superuser:

            return redirect('manager:choice')
        else:

            return redirect('start:read')

    return render(request, 'start/home.html', {})


@login_required(login_url='manager:login')
def register_student_view(request):
    ''' this method registered a student '''

    if request.user.is_superuser:

        form = RegisterStudentForm(request.POST or None)
        if form.is_valid():

            form.save()
            messages.success(request, 'Registration Successful')
            form = RegisterStudentForm()

        return render(request, 'start/register.html', {'form': form})
    else:

        return HttpResponse('<h1>You are not authorized to see this page<h1>')


def login_student_view(request):
    ''' this method check login status of student '''

    if request.user.is_authenticated:

        if request.user.is_superuser:

            return redirect('manager:choice')
        else:

            return redirect('start:read')

    form = LoginStudentForm(request.POST or None)

    if request.method == 'POST':

        username = request.POST.get('student_name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('start:read')
        else:

            print('failed')

    return render(request, 'start/login.html', {'form': form})


@login_required(login_url='start:login')
def logout_student_view(request):
    ''' this method logout the student '''

    if request.user.is_superuser:
        return redirect('manager:choice')

    print('hello')
    logout(request)
    return redirect('start:login')


@login_required(login_url='start:login')
def issued_view(request):
    ''' this method list out the issued book by current user '''

    if request.user.is_superuser:
        return redirect('manager:choice')

    list_of_book = IssueBook.objects.filter(student_name=request.user)
    return render(request, 'start/issued.html', {'list_of_book': list_of_book})


@login_required(login_url='start:login')
def read_view(request):
    ''' this method work to read all books '''

    book_obj = Books.objects.all()
    return render(request, 'start/read.html', {'book_obj': book_obj})


@login_required(login_url='start:login')
def search_view(request):
    ''' this method work to search a specific book '''
    book = request.GET.get('book_search')
    book_obj = Books.objects.filter(book_name=book)
    return render(request, 'start/read.html', {'book_obj': book_obj})
