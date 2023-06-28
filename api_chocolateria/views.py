from django.shortcuts import render
from .models import Producto
from .serializer import ProductoSerializer
#clases propias de la api
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
##PARA LA AUTENTICACION
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

##PARA LAS FUNCIONES
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

csrf_exempt
@api_view(['GET','POST'])
#@permission_classes((IsAuthenticated,))
def lista_Productos(request):
    ##siempre se pregunta que tipo de metodo es el que trabajara
    if request.method =='GET':
        query=Producto.objects.all()
        serializer = ProductoSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method =='POST': 
         serializer = ProductoSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
         else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)      

@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))  
def detalle_Producto(request, id):
    try:
        producto =Producto.objects.get(nombre=id)
    except producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    if request.method =='GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    if request.method =='PUT':
        serializer = ProductoSerializer(producto, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    if request.method =='DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario Invalido") 

    pass_valida =check_password(password, user.password)

    if not pass_valida:
        return Response("Password Incorrecta")

    token, created = Token.objects.get_or_create(user=user)

    return Response(token.key)
