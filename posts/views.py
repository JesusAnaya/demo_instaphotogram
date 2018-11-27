from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from posts.serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
