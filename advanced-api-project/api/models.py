from django.db import models
from django.utils import timezone

# Author model to represent a writer
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model to represent a written book
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    # Year the book was published
    publication_year = models.IntegerField()
    # Relationship: one Author can have many Books
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.
