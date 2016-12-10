from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget



class PostForm(forms.ModelForm):
    articulo = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ['portada','titulo','autor','subtitulo','seccion', 'articulo']
