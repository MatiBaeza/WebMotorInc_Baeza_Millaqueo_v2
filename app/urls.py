from django.urls import path
from . views import index, servicios, galeria, productos, ubicacion, contacto, register, registrarPaquete, eliminarPaquete, edicionPaquete, editarPaquete

urlpatterns = [
    path('', index, name='index'),
    path('servicios/', servicios, name='servicios'),
    path('galeria/', galeria, name='galeria'),
    path('productos/', productos, name='productos'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('contacto/', contacto, name='contacto'),
    path('register/', register, name='register'),
    path('registrarPaquete/', registrarPaquete),
    path('productos/edicionPaquete/<codigo>', edicionPaquete),
     path('editarPaquete/', editarPaquete),
    path('productos/eliminarPaquete/<codigo>', eliminarPaquete),
]