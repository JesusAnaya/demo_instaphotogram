from django.urls import path, include
from posts.views import PostListCreateView, PostRetrieveUpdateDestroyView


urlpatterns = [
    path('', PostListCreateView.as_view(), name='api-posts'),
    path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='api-post'),
]
