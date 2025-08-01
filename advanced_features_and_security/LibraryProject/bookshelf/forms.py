from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookSearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)