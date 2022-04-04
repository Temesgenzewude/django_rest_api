from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

# class PostListView(generics.ListCreateAPIView):
#     # permission_classes=(permissions.IsAuthenticated,)

#     queryset=Post.objects.all()
#     serializer_class=PostSerializer

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes=(permissions.IsAuthenticated,)
#     permission_classes=(IsAuthorOrReadOnly,)
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadOnly,)

    queryset=Post.objects.all()
    serializer_class=PostSerializer

# class UserListView(generics.ListCreateAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer


# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer

