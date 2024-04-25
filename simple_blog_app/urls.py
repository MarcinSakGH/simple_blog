from django.urls import path

from simple_blog_app.views import PostListView, CreatePostView, PostDetailView, RemovePostView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('remove-post/<int:pk>/', RemovePostView.as_view(), name='remove-post'),
]