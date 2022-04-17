from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('multiplex', views.consultar_multiplex, name='consultar_multiplex'),
    path('multiplex/registrar', views.registrar_multiplex, name='registrar_multiplex'),
    path('sala', views.consultar_sala, name='consultar_sala'),
    path('sala/registrar', views.registrar_sala, name='registrar_sala'),
    path('usuario', views.registrar_usuario, name='registrar_usuario'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)