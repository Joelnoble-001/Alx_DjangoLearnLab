# Role-Based Access Control Setup for `bookshelf` App

This project uses Django's permission and group system to control access to views in the `bookshelf` app.

## Custom Permissions Defined (in `models.py`)

The following custom permissions were added to the `Book` model:

- `can_view`: Can view book list
- `can_create`: Can add books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

## User Groups and Permissions (created via shell)

### Viewers Group
- Has: `can_view`

### Editors Group
- Has: `can_view`, `can_create`, `can_edit`

### Admins Group
- Has: `can_view`, `can_create`, `can_edit`, `can_delete`

## Views and Access Control (in `views.py`)

Each view is decorated with `@permission_required` and restricted accordingly:

- `list_books` → `@permission_required('bookshelf.can_view')`
- `add_book` → `@permission_required('bookshelf.can_create')`
- `edit_book` → `@permission_required('bookshelf.can_edit')`
- `delete_book` → `@permission_required('bookshelf.can_delete')`

## Users

Created test users and assigned them to the appropriate groups:
- `viewer_user`: Viewers
- `editor_user`: Editors
- `admin_user`: Admins
