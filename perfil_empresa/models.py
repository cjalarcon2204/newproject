from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=70)
    telefono = models.IntegerField(max_length=9)
    estado = models.BooleanField(default= True)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "clientes"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"


    def __str__(self):
        return self.nombres + ' ' + self.apellidos



class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    ruc = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=200)
    razon_comercial = models.CharField(max_length=200)
    direccion = models.CharField(max_length=10)
    correo = models.EmailField(max_length=70)
    #general_empresa = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "empresa"
        verbose_name = "empresa"
        verbose_name_plural = "empresas"

    def __str__(self):
        return self.nombre

class Documentos(models.Model):
    sri = models.FileField(null = True, blank = True)
    iess = models.FileField(null = True, blank = True)
    niv_financiero = models.FileField(null = True, blank = True)
    niv_tributario = models.FileField(null = True, blank = True)
    niv_laboral = models.FileField(null = True, blank = True)
    trabajadores = models.FileField(null = True, blank = True)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "documentos"
        verbose_name = "documento"
        verbose_name_plural = "documentos"



class CategoriaServicios(models.Model):
    categorias = models.CharField(max_length=200)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categorias'
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.categorias


class Servicio(models.Model):
    tipo = models.CharField(max_length=200)
    cat_servicio = models.ForeignKey(CategoriaServicios, on_delete=models.CASCADE)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'servicios'
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.tipo


