from django.test import TestCase
from blog.models import Post


from django.test import TestCase
from blog.forms import PostForm
from blog.models import Post


from django.test import TestCase
from django.urls import reverse
from blog.models import Post

def test_post_creation(self):
    self.assertEqual(Post.objects.count(), 1)
    self.assertEqual(self.post.title, 'Título de prueba')
    self.assertEqual(self.post.author, 'Autor de prueba')

def test_listar_publicaciones_view(self):
    response = self.client.get(reverse('listar_publicaciones'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'blog/post_list.html')

def test_crear_post_view(self):
    self.client.login(username='testuser', password='password123')
    response = self.client.post(reverse('crear_post'), {
        'title': 'Nuevo post', 'subtitle': 'Subtítulo', 'content': 'Contenido de prueba'
    })
    self.assertEqual(Post.objects.count(), 2)
