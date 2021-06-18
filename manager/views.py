from django.shortcuts import redirect, render
from .forms import ManagerLoginForm, IssueBookForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.core.exceptions import ObjectDoesNotExist
from .models import IssueBook
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def manager_login_view(request):
    ''' this function login the user '''

    if request.user.is_authenticated:
        return redirect('manager:choice')

    form = ManagerLoginForm(request.POST or None)

    if form.is_valid():
        username = request.POST.get('manager_name')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if not user.is_superuser:
                return HttpResponse('<h1>You are not SuperUser<h1>')

            login(request, user)
            return redirect('manager:choice')
        else:
            messages.error(request, 'Password or username is Wrong')
    return render(request, 'Manager/login.html', {'form': form})


def manager_logout_view(request):
    ''' this function logout the user '''

    if request.method == 'POST':
        logout(request)
        return redirect('manager:login')


@login_required(login_url='manager:login')
def choice_view(request):
    ''' this function give the option to manger, create, read and more '''

    if request.user.is_superuser:
        return render(request, 'Manager/choice.html', {})
    else:
        return HttpResponse('<h1>You are not authorized to see this Page<h1>')


@login_required(login_url='manager:login')
def issue_book_view(request):
    ''' this function work to issue a book '''

    if request.user.is_superuser:
        form = IssueBookForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():

                try:
                    User.objects.get(username=request.POST.get('student_name'))

                except ObjectDoesNotExist:
                    messages.error(request, 'Student does not exist')
                    return redirect('start:register')

                form.save()
                messages.success(request, 'Book Issued Successfully')
                return redirect('manager:issue')
            else:

                messages.error(request, 'Data is not valid')

        return render(request, 'Manager/issue.html', {'form': form})
    else:

        return HttpResponse('<h1>You are not authorized to see this Page<h1>')


@login_required(login_url='manager:login')
def see_issue_book_view(request):
    ''' this function work to see all issue book '''

    if request.user.is_superuser:
        book = IssueBook.objects.all()
        return render(request, 'Manager/view.html', {'issue_book': book})
    else:

        return HttpResponse('<h1>You are not authorized to see this Page<h1>')


@login_required(login_url='manager:login')
def return_issue_book_view(request, id):
    ''' this function work to return issued books '''

    if request.user.is_superuser:
        return_book = IssueBook.objects.get(id=id)
        return_book.delete()
        return redirect('manager:viewissue')

    else:

        return HttpResponse('<h1>You are not authorized to see this Page<h1>')


@login_required(login_url='manager:login')
def search_view(request):
    ''' this function search the student name '''

    if request.user.is_superuser:
        if request.method == 'GET':
            student_name = request.GET.get('student_search')
            book = IssueBook.objects.filter(student_name=student_name)
            return render(request, 'Manager/view.html', {'issue_book': book})
    else:

        return HttpResponse('<h1>You are not authorized to see this Page<h1>')
