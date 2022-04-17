from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Multiplex, Sala
from .forms import RegistrarMultiplexForm, RegistrarUsuarioForm, RegistrarSalaForm


# Create your views here.
def index(request):
    return render(request, 'vistas/index.html')

'''def login(request):
    datos = Usuario.objects.all()
    return render(request, 'vistas/registrar_multiplex.html', {'data': datos})'''

def consultar_multiplex(request):
    multiplex = Multiplex.objects.all()
    return render(request, 'vistas/consultar_multiplex.html', {'multiplexs': multiplex})

def consultar_sala(request):
    salas = Sala.objects.all()
    return render(request, 'vistas/consultar_sala.html', {'salas': salas})

def registrar_multiplex(request):
    multiplexs = Multiplex.objects.all()
    formulario = RegistrarMultiplexForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registrar_multiplex')
    return render(request, 'vistas/registrar_multiplex.html', {'formulario': formulario}, {'multiplexs': multiplexs})

def registrar_sala(request):
    formulario = RegistrarSalaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registrar_sala')
    return render(request, 'vistas/registrar_sala.html', {'formulario': formulario})

def registrar_usuario(request):
    formulario = RegistrarUsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registrar_usuario')
    return render(request, 'vistas/registrar_usuario.html', {'formulario': formulario})

