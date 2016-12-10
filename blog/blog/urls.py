from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as autenticacion
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', autenticacion.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^summernote/',include('django_summernote.urls')),

    url(r'^$', 'post.views.inicio', name='inicio'),
    url(r'^Blog/post/nuevo/$', 'post.views.nuevo_post', name='post-nuevo'),
    url(r'^blog/post/detalle/(?P<id>\d+)', 'post.views.detalle_post', name='detalle-post'),
    url(r'^Blog/admin/lista/$', 'post.views.Lista_admin', name='lista'),
    url(r'^blog/admin/detalle/(?P<id>\d+)', 'post.views.detalle_admin', name='admin-detalle'),



)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

    urlpatterns += staticfiles_urlpatterns()
