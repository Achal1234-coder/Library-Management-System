from django.shortcuts import render
from .forms import RegisterStudentForm, LoginStudentForm
from .models import RegistrationStudent
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def home_view(request):
    ''' this function render the home.html '''

    return render(request, 'start/home.html', {})


def register_student_view(request):
    ''' this function registered a student '''

    form = RegisterStudentForm(request.POST or None)
    if form.is_valid():
        try:   # if id exist it return message error
            id = request.POST.get('student_id')
            RegistrationStudent.objects.get(student_id=id)
            messages.error(request, 'You are already Registered')
        except ObjectDoesNotExist:
            # if try through exception then it check if and else block

            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if password != confirm_password:
                messages.error(request, 'Password not match')
            else:
                obj = RegistrationStudent.objects.create(
                    student_name=request.POST.get('student_name'),
                    student_id=request.POST.get('student_id'),
                    password=request.POST.get('password')
                    )
                obj.save()
                messages.success(request, 'Registration Successful')
                form = RegisterStudentForm()
    return render(request, 'start/register.html', {'form': form})


def login_student_view(request):
    ''' this function check login status of student '''

    form = LoginStudentForm(request.POST or None)
    if form.is_valid():
        id = request.POST.get('student_id')
        obj = RegistrationStudent.objects.get(student_id=id)
        if obj.password != request.POST.get('password'):
            messages.error(request, 'Password Not Matched')
        else:
            print('Successful')
            form = LoginStudentForm()
    return render(request, 'start/login.html', {'form': form})
