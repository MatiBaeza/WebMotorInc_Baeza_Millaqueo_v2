from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from . models import Paquete
from app.carrito import Carrito

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

def tienda(request):
    paquete = Paquete.objects.all()
    return render(request, 'app/tienda.html', {"paquete" : paquete})  


def agregar_carrito(request, paquete_id):
    carrito = Carrito(request)
    paquete = Paquete.objects.get(id=paquete_id)  
    carrito.Add(paquete)
    return redirect('/tienda')  

def eliminar_carrito(request, paquete_id):
    carrito = carrito(request)
    paquete = Paquete.objects.get(id=paquete_id)
    carrito.Remove(paquete)
    return redirect('/tienda')

def restar_carrito(request, paquete_id):
    carrito = Carrito(request)
    paquete = Paquete.objects.get(id=paquete_id)
    carrito.Sub(paquete)
    return redirect('/tienda')   

def limpiar(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('/tienda')         

def contacto(request):
    return render(request, 'app/contacto.html')     
      
def registrarPaquete(request):
    id=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    imagen=request.FILE['txtImagen']
    precio=request.POST['numPrecio']

    paquete = Paquete.objects.create(
        id=id, nombre=nombre, precio=precio)   
    return redirect('/productos')

def edicionPaquete(request, id):
    paquete = Paquete.objects.get(id = id)
    return render(request, "app/edicionPaquete.html", {"paquete": paquete})

def editarPaquete(request):
    id=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    imagen=request.FILE['txtImagen']
    precio=request.POST['numPrecio']  

    paquete = Paquete.objects.get(id = id)
    paquete.nombre = nombre
    paquete.imagen = imagen
    paquete.precio = precio
    paquete.save()
 
    return redirect('/productos')       

def eliminarPaquete(request, id):
    paquete = Paquete.objects.get(id = id)
    paquete.delete()

    return redirect('/productos')
