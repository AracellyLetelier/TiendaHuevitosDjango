from django.shortcuts import render,redirect
from .models import Producto
from .form import ProductoForm
#from api_chocolateria.urls import login,detalle_Producto,lista_Productos

# Create your views here.

def index(request):
    return render(request,"htmls/index.html")

def Carrito(request):
    return render(request,"htmls/Carrito.html")

def Inicio_sesion(request):
    """ Login = login
    if Login.is_valid(): """
    return render(request,"htmls/admin/Inicio_sesion.html")

def Productos(request):
    Productos= Producto.objects.all()
    return render(request,"htmls/Productos.html",{"Productos":Productos})

def Registrate(request):
    return render(request,"htmls/Registrate.html")

def Nosotros(request):
    return render(request,"htmls/Nosotros.html")

def indexadmin(request):
    Productos= Producto.objects.all()
    return render(request,"htmls/admin/indexadmin.html" ,{"Productos":Productos})

def layoutAdmin(request):
    return render(request,"htmls/admin/layoutAdmin.html")

def form_savepro(request):
    form =ProductoForm
    mensaje = ""
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = request.POST.get('nombre', None)
            if nombre in Producto.objects.values_list('descripcion', flat=True):
                mensaje="Este nombre de Producto ya está registrado"
            else:
                form.save()
                mensaje="Datos Guardados Correctamente"    

    return render(request,"htmls/admin/form_savepro.html", {"form":form,"mensaje":mensaje})

def form_modpro(request, id):
    Product = Producto.objects.get(descripcion=id)
    mensaje=""
    if request.method == 'POST':
        form =ProductoForm(request.POST, request.FILES, instance=Product)
        if form.is_valid():
            form.save()
            mensaje = "Datos Modificado Correctamente"
            return redirect(to="indexadmin")
    else:
        return render(request, "htmls/admin/form_modpro.html", {"form":ProductoForm(instance=Product), "mensaje":mensaje})

def delete_Producto(request, id):
    Product = Producto.objects.get(descripcion=id)
    Product.delete()
    return redirect(to="indexadmin")

        

