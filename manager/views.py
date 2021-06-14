from django.shortcuts import redirect, render
from .forms import ManagerRegistrationForm, ManagerLoginForm
from django.contrib.auth.models import User
from django.contrib import messages


def manager_register_view(request):
    ''' this function registered manager with the help of admin '''

    form = ManagerRegistrationForm(request.POST or None)
    if form.is_valid():
        admin_password = request.POST.get('admin_password')
        name = request.POST.get('manager_name')
        password = request.POST.get('password1')
        user = User.objects.get(username='achal')  # achal is superuser
        if user.check_password(admin_password):
            new_user = User.objects.create_user(
                       username=name,
                       password=password
                    )
            new_user.save()
            messages.success(request, 'New Manager account created')
            form = ManagerRegistrationForm()
        else:
            messages.error(request, 'Admin Password Wrong')
    return render(request, 'Manager/Register.html', {'form': form})


def manager_login_view(request):
    ''' this function login the user '''

    form = ManagerLoginForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('book_manager_name')
        password = request.POST.get('password')
        user = User.objects.get(username=name)
        if user.check_password(password):
            return redirect('choice')
        else:
            messages.error(request, 'Password is Wrong')
    return render(request, 'Manager/login.html', {'form': form})


def choice_view(request):
    ''' this function give the option to manger, create or read '''
    
    return render(request, 'Manager/choice.html', {})
