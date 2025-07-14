## Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984>
```

## Retrieve

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title
# '1984'
book.author
# 'George Orwell'
book.publication_year
# 1949
```

## Update

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'
```

## Delete

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>
```
