from django.contrib import admin
from .models import Producto, CategoriaProd

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(CategoriaProd)

class productosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Producto)
