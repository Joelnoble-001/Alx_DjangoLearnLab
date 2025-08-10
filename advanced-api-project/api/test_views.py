from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create an author
        self.author = Author.objects.create(name='Test Author')

        # Create a book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )

        self.list_url = reverse('book-list')  # If using DRF routers
        self.detail_url = reverse('book-detail', args=[self.book.id])

    def test_list_books(self):
        """Test retrieving all books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a new book with authentication"""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book"""
        data = {
            "title": "Another Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test updating a book"""
        self.client.login(username='testuser', password='testpass')
        data = {
            "title": "Updated Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_authenticated(self):
        """Test deleting a book"""
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(f"{self.list_url}?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book['title'] == 'Test Book' for book in response.data))

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Test' in book['title'] for book in response.data))

    def test_order_books_by_year(self):
        """Test ordering books by publication_year"""
        Book.objects.create(title='Older Book', publication_year=1990, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
