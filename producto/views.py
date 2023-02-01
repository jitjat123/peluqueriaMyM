from django.shortcuts import render
from producto.models import Producto
# Create your views here.


def productos(request):
    productos=Producto.objects.all()
    return render(request, "productos/productos.html", {"productos": productos})