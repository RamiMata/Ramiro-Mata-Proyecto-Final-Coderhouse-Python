from django.urls import path
from . import views  # Importamos las vistas de la app

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista principal
    path('crear/', views.crear_post, name='crear_post'),
    path('posts/', views.listar_publicaciones, name='listar_publicaciones'),
    path('<int:pk>/', views.post_detail, name='post_detail'),  # Detalles de la publicación
    path('update/<int:pk>/', views.post_update, name='post_update'),  # Editar publicación
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),  # Eliminar publicación
    path('about/', views.about, name='about'),
    path('post_user/<int:pk>/', views.post_detail_user_view, name='post_detail_user'),
]

