from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from posts.models import Post
from posts.serializers import PostSerializer, PostPhotoSerializer
from posts.permissions import IsOwner


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

    def create(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            # Assign the currently logged user as the owner
            serializer.save(owner=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, parser_classes=(MultiPartParser, FormParser))
    def upload_photo(self, request, pk=None):
        post = self.get_object()
        serializer = PostPhotoSerializer(post, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def like(self, request, pk=None):
        post = self.get_object()
        post.increase_likes()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
