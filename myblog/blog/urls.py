from django.urls import path
from . import views
from .views import postsListView, postsDetailView, postsCreateView, postsUpdateView, postsDeleteView, UserpostsListView

urlpatterns = [
    path('', postsListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserpostsListView.as_view(), name='user-posts'),
    path('posts/<int:pk>/', postsDetailView.as_view(), name='posts-detail'),
    path('posts/<int:pk>/update', postsUpdateView.as_view(), name='posts-update'),
    path('posts/<int:pk>/delete', postsDeleteView.as_view(), name='posts-delete'),
    path('posts/new/', postsCreateView.as_view(), name='posts-create'),
    path('about/', views.about, name='blog-about')
]
