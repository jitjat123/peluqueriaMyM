from django.urls import path
from . import views


app_name="carro"

urlpatterns = [

    path('',views.carrito,name="Carro"),
    path("agregar/<int:producto_id>/",views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/",views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/",views.restar_producto, name="restar"),
    path("limpiar/",views.limpiar_carro, name="limpiar"),
    path("actualizar/<int:producto_id>/<int:cantidad>/",views.actualizar_carro, name="actualizar"),


]