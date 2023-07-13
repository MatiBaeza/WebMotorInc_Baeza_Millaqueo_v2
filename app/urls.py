from django.urls import path
from . views import index, servicios, galeria, productos, ubicacion, tienda, agregar_carrito, eliminar_carrito, restar_carrito, limpiar, contacto, registrarPaquete, eliminarPaquete, edicionPaquete, editarPaquete

urlpatterns = [
    path('', index, name='index'),
    path('servicios/', servicios, name='servicios'),
    path('galeria/', galeria, name='galeria'),
    path('productos/', productos, name='productos'),
    path('ubicacion/', ubicacion, name='ubicacion'),
    path('tienda/', tienda, name='tienda'),
    path('Add/<int:paquete_id>/', agregar_carrito, name='Add'),
    path('Remove/<int:paquete_id>/', eliminar_carrito, name='Del'),
    path('Sub/<int:paquete_id>/', restar_carrito, name='Sub'),
    path('limpiar/', limpiar, name='Cls'),
    path('contacto/', contacto, name='contacto'),
    path('registrarPaquete/', registrarPaquete),
    path('productos/edicionPaquete/<id>', edicionPaquete),
    path('editarPaquete/', editarPaquete),
    path('productos/eliminarPaquete/<id>', eliminarPaquete),
]