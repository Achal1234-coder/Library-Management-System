from django.shortcuts import redirect, render
from .forms import Manager_Registration_form, Manager_login_form
from django.contrib.auth.models import User
from django.contrib import messages


def manager_register_view(request):
    form = Manager_Registration_form(request.POST or None)
    if form.is_valid():
        admin_password = request.POST.get('Admin_Password')
        name = request.POST.get('Manager_Name')
        password = request.POST.get('password1')
        user = User.objects.get(username='achal')  # achal is superuser
        if user.check_password(admin_password):
            new_user = User.objects.create_user(
                       username=name,
                       password=password
                    )
            new_user.save()
            messages.success(request, 'New Manager account created')
            form = Manager_Registration_form()
        else:
            messages.error(request, 'Admin Password Wrong')
    return render(request, 'Manager/Register.html', {'form': form})


def manager_login_view(request):
    form = Manager_login_form(request.POST or None)
    if form.is_valid():
        name = request.POST.get('Book_Manager_Name')
        password = request.POST.get('Password')
        user = User.objects.get(username=name)
        if user.check_password(password):
            return redirect('choice')
        else:
            messages.error(request, 'Password is Wrong')
    return render(request, 'Manager/login.html', {'form': form})


def choice_view(request):
    return render(request, 'Manager/choice.html', {})
