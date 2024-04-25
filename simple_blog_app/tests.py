from django.test import Client
import pytest
from django.urls import reverse
from .models import Post

# Create your tests here.


@pytest.fixture
def my_post():
    my_post = Post.objects.create(title='Test post title', content='Test post content')
    return my_post

@pytest.mark.django_db
def test_post_list_view(my_post, client):
    response = client.get(reverse('post-list'))
    assert response.status_code == 200
    assert 'Test post title' in response.content.decode()

@pytest.mark.django_db
def test_post_detail_view(my_post, client):
    response = client.get(reverse('post-detail', kwargs={'pk': my_post.pk}))
    assert response.status_code == 200
    assert 'Test post content' in response.content.decode()

@pytest.mark.django_db
def test_post_create_view(client):
    response = client.post(reverse('create-post'), data={'title': 'Test post', 'content': 'Test post content'})
    assert response.status_code == 302
    assert Post.objects.filter(title='Test post').exists()

@pytest.mark.django_db
def test_post_update_view(my_post, client):
    response = client.post(reverse('edit-post', kwargs={'pk': my_post.pk}),
                           data={'title': 'new title', 'content': 'new content'})
    assert response.status_code == 302
    my_post.refresh_from_db()
    assert my_post.title == 'new title'
    assert my_post.content == 'new content'
