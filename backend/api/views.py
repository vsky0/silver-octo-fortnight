from django.shortcuts import render
from django.contrib.auth.models import User

from  rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer, NoteSerializer

from .models import Note
# Create your views here.

class CreateUserView(generics.CreateAPIView):
    query_set = User.objects.all() # providing all the user info, while creating user, so we can't repeat.
    serializer_class = UserSerializer # what kind of data should be serialized.
    permission_class = [AllowAny] # permission to anyone.

# Create Notes
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user #get the authenticated user's notes
        return Note.objects.filter(author=user) #filter notes by user itself
    
    def perform_create(self, serializer):
        if serializer.is_valid(): #check if serializer object is valid or not
            serializer.save(author=self.request.user) # if user is authenticated, then get user info, as we get to read user.
        else:
            print(serializer.errors)

# Delete Notes
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)