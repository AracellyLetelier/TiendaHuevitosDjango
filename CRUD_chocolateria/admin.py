from django.contrib import admin
from .models import Categoria,Producto,Usuarios,Boleta

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Usuarios)
admin.site.register(Boleta)