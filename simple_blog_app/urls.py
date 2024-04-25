from django.urls import path

from simple_blog_app.views import PostListView

urlpatterns = [
    path('post-list/', PostListView.as_view(), name='post-list'),
]