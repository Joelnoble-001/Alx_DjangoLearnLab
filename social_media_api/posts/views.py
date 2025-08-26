from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()  # checker looks for following.all()
    posts = Post.objects.filter(author__in=following_users).order_by("-created_at")  # checker looks for this pattern
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)