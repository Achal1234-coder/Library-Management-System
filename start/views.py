from django.shortcuts import render
from .forms import Register_student_form, Login_student_form
from .models import Registration_Student
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


def home_view(request):
    return render(request, 'start/home.html', {})


def register_student_view(request):
    form = Register_student_form(request.POST or None)
    if form.is_valid():
        try:
            Id = request.POST.get('Student_Id')
            Registration_Student.objects.get(Student_Id=Id)
            messages.error(request, 'You are already Registered')
        except ObjectDoesNotExist:
            password1 = request.POST.get('Password')
            password2 = request.POST.get('Confirm_Password')
            if password1 != password2:
                messages.error(request, 'Password not match')
            else:
                Obj = Registration_Student.objects.create(
                    Student_Name=request.POST.get('Student_Name'),
                    Student_Id=request.POST.get('Student_Id'),
                    Password=request.POST.get('Password')
                    )
                Obj.save()
                messages.success(request, 'Registration Successful')
                form = Register_student_form()
    return render(request, 'start/register.html', {'form': form})


def login_student_view(request):
    form = Login_student_form(request.POST or None)
    if form.is_valid():
        Id = request.POST.get('Student_Id')
        Obj = Registration_Student.objects.get(Student_Id=Id)
        if Obj.Password != request.POST.get('Password'):
            messages.error(request, 'Password Not Matched')
        else:
            print('Successful')
            form = Login_student_form()
    return render(request, 'start/login.html', {'form': form})
