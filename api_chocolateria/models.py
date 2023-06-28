from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    Stock = models.IntegerField()
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    file =  models.ImageField(upload_to="Productos")

    def __str__(self):
        return self.descripcion

class Usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=60)
    edad = models.IntegerField()
    correo =models.CharField(max_length=50)
    nombreUsuario = models.CharField(max_length=50)
    claveUsuario= models.CharField(max_length=15)

    def __str__(self):
        return self.nombreUsuario

class Boleta(models.Model):
    idBoleta = models.AutoField(primary_key=True)
    fechaBoleta= models.DateField()
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    Cantidad = models.IntegerField()
    idUsuario= models.ForeignKey(Usuarios,on_delete=models.CASCADE)

    def __str__(self):
        return self.idBoleta
