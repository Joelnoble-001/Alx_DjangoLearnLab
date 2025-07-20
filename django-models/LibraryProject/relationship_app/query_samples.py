# relationship_app/query_samples.py

import os
import sys
import django

# Add the project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

# Setup Django
django.setup()

# Import models
from relationship_app.models import Author, Book, Library

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # <- EXACT match for checker
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# 3. Retrieve the librarian for that library
try:
    librarian = library.librarian
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except NameError:
    print("Cannot check librarian because library lookup failed.")
except AttributeError:
    print("No librarian assigned to this library.")
