from django.shortcuts import render
from rest_framework import generics, viewset
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewset.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer