from django.urls import path
from . import views
from .views import form_example_view

# URL patterns for the bookshelf app
urlpatterns = [
    path('', views.book_list, name='list_books'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('form-example/', form_example_view, name='form_example'),
]