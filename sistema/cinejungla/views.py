from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Usuario, Multiplex, Sala
from .forms import RegistrarMultiplexForm, RegistrarUsuarioForm, RegistrarSalaForm

# Create your views here.
def index(request):
    return render(request, 'vistas/index.html')        

def consultar_multiplex(request):
    multiplex = Multiplex.objects.all()
    return render(request, 'vistas/consultar_multiplex.html', {'multiplexs': multiplex})

def consultar_sala(request):
    multiplexs = Multiplex.objects.all()
    salas = Sala.objects.all()
    return render(request, 'vistas/consultar_sala.html', {'salas': salas, 'multiplexs': multiplexs})

def registrar_multiplex(request):
    formulario = RegistrarMultiplexForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('consultar_multiplex')
    return render(request, 'vistas/registrar_multiplex.html', {'formulario': formulario})

def registrar_sala(request):
    multiplexs = Multiplex.objects.all()
    formulario = RegistrarSalaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('consultar_sala')
    return render(request, 'vistas/registrar_sala.html', {'formulario': formulario, 'multiplexs': multiplexs})

def registrar_usuario(request):
    multiplexs = Multiplex.objects.all()
    formulario = RegistrarUsuarioForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('registrar_usuario')
    return render(request, 'vistas/registrar_usuario.html', {'formulario': formulario,'multiplexs': multiplexs})

