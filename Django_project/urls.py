"""Django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from start.views import home_view, register_student_view, login_student_view
from manager.views import manager_register_view, manager_login_view, choice_view
from book.views import create_book_view, read_book_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('register', register_student_view, name='register'),
    path('login', login_student_view, name='login'),
    path('Register', manager_register_view, name='Manager_Registration'),
    path('login-manager', manager_login_view, name='manager_login'),
    path('choice', choice_view, name='choice'),
    path('create-book', create_book_view, name='create-book'),
    path('Read', read_book_view, name='read-book')
]
