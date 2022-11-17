from email import message
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import usuarios , Registros
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib import messages


def index(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def logincheck(request):
  perfiles = Registros.objects.all().values()
  username = request.POST['username']
  password = request.POST['password']
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def register(request):
    usuarios_ = usuarios.objects.all().values()
    template = loader.get_template('register.html')
    context = {
        'usuarios': usuarios_,
    }
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('addUser.html')
  return HttpResponse(template.render({}, request))

def addUsuario(request):
  primerN = request.POST['primerNombre']
  segundoN = request.POST['segundoNombre']
  apellido = request.POST['apellido']
  edad_ = request.POST['edad']
  usuario = usuarios(primer_nombre = primerN,
    segundo_nombre = segundoN,
    apellidos = apellido,
    edad = edad_)
  usuario.save()
  return HttpResponseRedirect(reverse('register'))

def deleteUsuario(request, id):
  usuarios_ = usuarios.objects.get(id=id)
  usuarios_.delete()
  return HttpResponseRedirect(reverse('register'))