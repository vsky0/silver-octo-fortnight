from django.shortcuts import render
from django.contrib.auth.models import User
from  rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    query_set = User.objects.all() # providing all the user info, while creating user, so we can't repeat.
    serializer_class = UserSerializer # what kind of data should be serialized.
    permission_class = [AllowAny] # permission to anyone.
