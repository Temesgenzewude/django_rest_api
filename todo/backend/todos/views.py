from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class ListTodoView(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class DetailTodoView(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

