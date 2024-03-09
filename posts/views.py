from .serializers import PostSerializers, UserSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework import viewsets


# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = IsAuthorOrReadOnly,
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
