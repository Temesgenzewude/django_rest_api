from django.urls import path
from .views import ListTodoView, DetailTodoView

urlpatterns=[
    path('<int:pk>/', DetailTodoView.as_view() ),
    path('', ListTodoView.as_view()),
]