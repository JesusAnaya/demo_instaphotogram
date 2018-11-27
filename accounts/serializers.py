from rest_framework import serializers


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=200)
