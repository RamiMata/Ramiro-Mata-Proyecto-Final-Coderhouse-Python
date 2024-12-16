"""
URL configuration for proyecto_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog import views


# Definición del manejador de errores 404
from django.conf.urls import handler404

handler404 = 'proyecto_blog.views.pagina_no_encontrada'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # URLs de blogs
    path('accounts/', include('cuentas.urls')),  # URLs de cuentas
    path('messages/', include('mensajeria.urls')),  # URLs de mensajería
    path('error/no-permisos/', views.error_no_permisos, name='error_no_permisos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
