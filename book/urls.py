from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('create', views.create_book_view, name='create'),
    path('read', views.read_book_view, name='read'),
    path('update/<int:book_id>', views.update_book_view, name='update'),
    path('delete/<int:book_id>', views.delete_book_view, name='delete'),
    path('search', views.search_view, name='search')

]
