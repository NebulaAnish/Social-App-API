from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Post, Comment, Profile
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, IsOwner

from .serializers import PostSerializer, CommentSerializer, ProfileSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # current_post = request.post
    # queryset = Comment.objects.filter(post=current_post)
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_queryset(self):
        current_post_id = self.kwargs['related_post']
        queryset = Comment.objects.filter(related_post=current_post_id)
        return queryset

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]

    def get_object(self):
        return self.request.user.profile
    