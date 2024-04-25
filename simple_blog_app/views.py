from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'


class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'create_post.html'
    success_url = reverse_lazy('post-list')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_details.html'

class RemovePostView(DeleteView):
    model = Post
    template_name = 'remove_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post-list')

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')