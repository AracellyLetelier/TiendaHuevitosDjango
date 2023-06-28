from django.urls import path
from .views import index ,Registrate,Productos,Carrito,Nosotros,Inicio_sesion,indexadmin,form_savepro,form_modpro,delete_Producto
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #aqui especifica que el index sera el index
    path('',index,name='index'),
    path('Registrate/',Registrate,name='Registrate'),
    path('Productos/',Productos,name='Productos'),
    path('Carrito/',Carrito,name='Carrito'),
    path('Nosotros/',Nosotros,name='Nosotros'),
    path('Inicio_sesion/',LoginView.as_view(template_name="htmls/admin/Inicio_sesion.html"),name='Inicio_sesion'),
    path('Fuera_sesion/',LogoutView.as_view(template_name="htmls/Index.html"),name='Fuera_sesion'),
    path('indexadmin/',indexadmin,name='indexadmin'),
    path('form_savepro/',form_savepro,name='form_savepro'),
    path('form_modpro/<id>',form_modpro,name='form_modpro'),
    path('delete_Producto/<id>',delete_Producto,name='delete_Producto'),   
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
