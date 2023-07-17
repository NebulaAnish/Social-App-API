from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.PostList.as_view(), name='postlist'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='postdetail'),
    path('accounts/profile/', views.ProfileDetail.as_view(), name='profiledetail'),
    # path('posts/<int:pk>/',)
    path('', include('rest_framework.urls')),
]