from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('login', views.manager_login_view, name='login'),
    path('choice', views.choice_view, name='choice'),
    path('logout', views.manager_logout_view, name='logout'),
    path('issue', views.issue_book_view, name='issue'),
    path('viewissue', views.see_issue_book_view, name='viewissue'),
    path('return/<int:id>', views.return_issue_book_view, name='return'),
    path('search', views.search_view, name='search')
]
