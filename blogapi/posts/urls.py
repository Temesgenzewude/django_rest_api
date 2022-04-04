from django.urls import path
# from .views import PostListView, PostDetailView, UserListView, UserDetailView
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

# urlpatterns=[
#     path('users/', UserListView.as_view()),
#     path('users/<int:pk>/', UserDetailView.as_view()),
#     path('<int:pk>/', PostDetailView.as_view()),
#     path('', PostListView.as_view()),

# ]
router=SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns=router.urls