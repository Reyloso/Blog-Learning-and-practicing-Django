from django.contrib import admin
from .models import Post,Seccion
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


class post (SummernoteModelAdmin):
	list_display = ['id','autor','titulo','subtitulo','seccion','articulo']
	class Meta:
		model = Post

class seccion (admin.ModelAdmin):
	list_display = ['id', 'seccion']
	class Meta:
		model = Seccion

admin.site.register(Post,post)
admin.site.register(Seccion,seccion)
