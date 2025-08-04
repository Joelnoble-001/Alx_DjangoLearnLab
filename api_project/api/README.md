## Authentication and Permissions

- Token Authentication is used via `rest_framework.authtoken`.
- Obtain a token via POST to `/api-token-auth/` with username & password.
- All API endpoints require the token via the `Authorization: Token <token>` header.
- Permission used: `IsAuthenticated` — only logged-in users can access the BookViewSet.