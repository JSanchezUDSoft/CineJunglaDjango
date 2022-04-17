from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.login, name='login'),
    path('multiplex', views.consultar_multiplex, name='consultar_multiplex'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)