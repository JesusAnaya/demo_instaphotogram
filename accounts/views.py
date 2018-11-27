from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import CreateUserSerializer


class CreateUser(APIView):
    def post(self, request, *args, **kwargs):
        """
        Create new user.
        """
        serializer = CreateUserSerializer(data=request.data)

        if serializer.is_valid():
            user, created = User.objects.get_or_create(username=serializer.data['username'])

            # Validate if user exists, return bad request. HTTP Code 409 Conflict
            if created:
                user.set_password(serializer.data['password'])
                user.save()

                response_data = {
                    'id': user.id,
                    'username': user.username
                }
                return Response(response_data, status=status.HTTP_200_OK)

            else:
                return Response({'error': 'USER_ALREADY_EXISTS'}, status=status.HTTP_409_CONFLICT)

        # Validate errors in POST data
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
