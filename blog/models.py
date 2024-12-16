from django.db import models



class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200, blank=True, null=True)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    author =  models.CharField(max_length=100,blank=True, null=True) 

    def __str__(self):
        return self.titulo
