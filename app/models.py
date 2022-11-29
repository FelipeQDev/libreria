from django.db import models

# Create your models here.
class Idioma(models.Model):
    nombre = models.CharField(max_length=45)
    url_imagen = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    url_imagen = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    nombre = models.CharField(max_length=45)
    fono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    rut = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)

    def __str__(self):
        return self.username

class Libro(models.Model):
    titulo = models.CharField(max_length=45)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    url_imagen = models.CharField(max_length=1000)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    stock = models.IntegerField()
    anio = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo


class Detalle(models.Model):
    fecha_pedido = models.DateTimeField()
    precio_total = models.IntegerField()




    

