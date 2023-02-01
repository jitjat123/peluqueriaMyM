from django.shortcuts import render, redirect

from .carro import Carro

from producto.models import Producto


# Create your views here.


def carrito(request):
    return render(request, "carro/carrito.html")

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.agregar(producto=producto)

    return redirect("Productos")


def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.eliminar(producto=producto)

    return redirect("Productos")

def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.restar_producto(producto=producto)

    return redirect("Productos")

def limpiar_carro(request):

    carro=Carro(request)

    carro.limpiar_carro()

    return redirect("Productos")

def actualizar_carro(request, producto_id, cantidad):
    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)

    carro.actualizar_carro(producto=producto, cantidad=cantidad)

    return redirect("carro:Carro")

    