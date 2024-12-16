from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'blog/index.html')

def es_admin(user):
    return user.is_authenticated and user.is_staff

def error_no_permisos(request):
    return render(request, 'error/no_permisos.html')

@user_passes_test(es_admin, login_url='/error/no-permisos/')
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Manejar imágenes
        if form.is_valid():
            form.save()
            return redirect('listar_publicaciones')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})

@user_passes_test(es_admin, login_url='/error/no-permisos/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@user_passes_test(es_admin, login_url='/error/no-permisos/')
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form, 'post': post})

@user_passes_test(es_admin, login_url='/error/no-permisos/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('listar_publicaciones')  
    return render(request, 'blog/post_delete.html', {'post': post})

def listar_publicaciones(request):
    publicaciones = Post.objects.all()
    return render(request, 'blog/post_list.html', {'publicaciones': publicaciones})


def about(request):
    return render(request, 'blog/about.html')

from django.shortcuts import get_object_or_404, render
from .models import Post

def post_detail_user_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail_user.html', {'post': post})
