from django.urls import path
from . import views

app_name = 'start'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('register', views.register_student_view, name='register'),
    path('login', views.login_student_view, name='login'),
    path('logout', views.logout_student_view, name='logout'),
    path('issued', views.issued_view, name='issued'),
    path('read', views.read_view, name='read'),
    path('search', views.search_view, name='search')
]
