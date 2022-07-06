from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    List all users
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a User instance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer