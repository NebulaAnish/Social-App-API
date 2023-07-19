from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Post, Comment, Profile
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action      
from .permissions import IsOwnerOrReadOnly, IsOwner

from .serializers import PostSerializer, CommentSerializer, ProfileSerializer
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

    @action(detail=True, methods=['POST'])
    def create_comment(self, request, pk=None):
        try:
            post = self.get_object()
        except Post.DoesNotExist:
            return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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



# Create your views here.

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     @action(detail=True, methods=['POST'])
#     def create_comment(self, request, pk=None):
#         try:
#             post = self.get_object()
#         except Post.DoesNotExist:
#             return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(post=post)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     serializer_class = CommentSerializer
#     queryset = Comment.objects.all()

#     def retrieve(self,request,pk=None):
#         try:
#             post = Post.objects.get(pk=pk)

#         except:
#             return Response({"error":"Post Not Found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     def create_comment(self,request, pk=None):
#         serializer.save(owner=self.request.user)
    