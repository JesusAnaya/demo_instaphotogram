from django.urls import path
from rest_framework.authtoken import views
from accounts.views import CreateUser, CurrentUser


urlpatterns = [
    path('api-token/', views.obtain_auth_token),
    path('create-user/', CreateUser.as_view()),
    path('current-user/', CurrentUser.as_view()),
]
