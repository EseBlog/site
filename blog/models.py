from django.db import models

# Create your models here.
class General(models.Model):
    creacion= models.DateField(auto_now=True) 
    actualizacion= models.DateTimeField(auto_now_add=True)
    nombre= models.CharField(max_length=264) 
    creador= models.CharField(max_length=264)
    tiktok= models.CharField(max_length=264, blank=True, null=True)
    facebook= models.CharField(max_length=264, blank=True, null=True)
    correo= models.CharField(max_length=264, blank=True, null=True)
    descripcion= models.TextField()

    class Meta:
        verbose_name_plural= 'Información General'

    def __str__(self):
        return self.nombre

class Materia(models.Model):
    creacion= models.DateField(auto_now=True)
    materia= models.CharField(max_length=264)
    actualizacion= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.materia
    
class Etiqueta(models.Model):
    creacion= models.DateField(auto_now=True)
    etiqueta= models.CharField(max_length=264)
    actualizacion= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.etiqueta
    
class Post(models.Model):
    creacion= models.DateField(auto_now=True)
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE, blank=True, null=True)
    titulo= models.CharField(max_length=264) 
    subtitulo= models.CharField(max_length=264, blank=True, null=True)
    autor= models.CharField(max_length=264)
    body= models.TextField()
    materia= models.ForeignKey(Materia, on_delete=models.CASCADE)
    actualizacion= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
