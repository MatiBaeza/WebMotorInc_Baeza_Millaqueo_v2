from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from . models import Paquete

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def galeria(request):
    return render(request, 'app/galeria.html')

@login_required
def productos(request):
    paquete = Paquete.objects.all()
    return render(request, 'app/productos.html', {"paquete" : paquete})  

def ubicacion(request):
    return render(request, 'app/ubicacion.html')

def contacto(request):
    return render(request, 'app/contacto.html')     

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html',data)           

def registrarPaquete(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio=request.POST['numPrecio']

    paquete = Paquete.objects.create(
        codigo=codigo, nombre=nombre, precio=precio)    
    return redirect('/productos')

def edicionPaquete(request, codigo):
    paquete = Paquete.objects.get(codigo = codigo)
    return render(request, "app/edicionPaquete.html", {"paquete": paquete})

def editarPaquete(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    precio=request.POST['numPrecio']  

    paquete = Paquete.objects.get(codigo = codigo)
    paquete.nombre = nombre
    paquete.precio = precio
    paquete.save()

    return redirect('/productos')       

def eliminarPaquete(request, codigo):
    paquete = Paquete.objects.get(codigo = codigo)
    paquete.delete()

    return redirect('/productos')
