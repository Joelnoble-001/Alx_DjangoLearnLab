from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    
    # ListAPIView endpoint (optional if still needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Router-generated endpoints for CRUD
    path('', include(router.urls)),

]