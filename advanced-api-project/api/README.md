# API Endpoints
- GET /api/books/ → List all books (public)
- GET /api/books/<id>/ → Get single book details (public)
- POST /api/books/create/ → Create new book (auth required)
- PUT /api/books/<id>/update/ → Update book (auth required)
- DELETE /api/books/<id>/delete/ → Delete book (auth required)

Permissions:
- Unauthenticated users → Read-only access
- Authenticated users → Full CRUD access
