from django.urls import path
from .views import detalle_Producto,lista_Productos,login
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[  
    path('lista_Productos', lista_Productos, name="lista_Productos"),
    path('detalle_Producto/<id>', detalle_Producto, name="detalle_Producto"),
    path('login', login, name="login"),

]