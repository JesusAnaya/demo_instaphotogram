from django.urls import path, include
from posts.views import PostListCreateView


urlpatterns = [
    path('', PostListCreateView.as_view(), name='api-posts'),
]
