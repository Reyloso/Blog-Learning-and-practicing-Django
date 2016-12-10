from django.db import models
from django.contrib.auth.models import User



class Seccion(models.Model):
    seccion = models.CharField(max_length=140)
    def __unicode__(self):
        return unicode(self.seccion)


class Post(models.Model):
    portada = models.ImageField(upload_to ='covers', verbose_name='Cover', null=True, blank=True)
    titulo = models.CharField(max_length=140)
    autor = models.ForeignKey(User, null=True, blank=True)
    subtitulo = models.CharField(max_length=140)
    seccion = models.ForeignKey(Seccion)
    articulo = models.TextField()
    def __unicode__(self):
        return unicode(self.titulo)
