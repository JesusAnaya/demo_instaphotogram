from django.urls import path, include
from rest_framework import routers
from posts.views import PostsViewSet


router = routers.SimpleRouter()
router.register('posts', PostsViewSet)

urlpatterns = router.urls
