from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm, BookSearchForm, ExampleForm 
# Create your views here.

# can view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

# can create
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

# can edit
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})

# can delete
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

def search_books(request):
    form = BookSearchForm(request.GET)
    books = Book.objects.none()
    if form.is_valid():
        books = Book.objects.filter(title__icontains=form.cleaned_data["q"])
    return render(request, "bookshelf/book_list.html", {"form": form, "books": books})

@csrf_protect
def example_form_view(request):
    """
    Handles the display and processing of a simple book submission form.
    If the request method is POST, retrieves the 'title' and 'author' fields from the form data.
    If both fields are provided, creates a new Book instance and displays a success message.
    If either field is missing, displays an error message indicating both fields are required.
    Renders the 'bookshelf/form_example.html' template with an optional message.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: The rendered form template with an optional message.
    """
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()

        if title and author:
            Book.objects.create(title=title, author=author)
            message = "Book added successfully!"
        else:
            message = "Both fields are required."

    return render(request, "bookshelf/form_example.html", {"message": message})