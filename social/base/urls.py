from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('', views.PostList.as_view(), name='postlist'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('accounts/profile/', views.ProfileDetail.as_view(), name='profiledetail'),
    # path('posts/<int:pk>/',)
    path('', include('rest_framework.urls')),
    # path('',include(router.urls)),
]
# urlpatterns +=router.urls