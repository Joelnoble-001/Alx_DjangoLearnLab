from django.shortcuts import render
from .models import Book 
from .models import Library 
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


# Function-Based View
def list_books(request):
    books = Book.objects.all() 
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Custom registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Built-in login view with template override
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Built-in logout view with template override
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'