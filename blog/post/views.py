from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

def inicio(request):

    a = Post.objects.all()
    return render(request,"post/inicio.html",{'a':a})
@login_required ( login_url = '/login/' )
def nuevo_post(request):
    form_post = PostForm()
    if request.method == "POST":
        form_post = PostForm(request.POST, request.FILES)
        if form_post.is_valid():
            formulario = form_post.save(commit=False)
            formulario.autor = request.user
            formulario.save()
            a = Post.objects.all()
            return render(request, "post/lista_post.html", {"a":a})
        else:
            print form_post.errors

    return render(request,"post/nuevo_post.html",{"form_post":form_post})

def detalle_post(request, id):

    a = get_object_or_404(Post, pk=id)

    return render(request, 'post/post_detalle.html', {'a':a})
def detalle_admin(request, id):

    i = get_object_or_404(Post, pk=id)

    return render(request, 'post/detalle_admin.html', {'i':i})


#listar post admin
@login_required ( login_url = '/login/' )
def Lista_admin(request):

    a = Post.objects.all()
    return render(request,"post/lista_post.html",{'a':a})
