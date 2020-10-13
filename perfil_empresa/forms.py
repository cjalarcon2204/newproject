from django import forms
from .models import Empresa, Cliente, Servicio, CategoriaServicios, Documentos

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombres", "apellidos", "correo", "direccion", "telefono", "estado"]

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nombre","ruc","razon_social","razon_comercial","direccion","correo"]

class DocumentosForm(forms.ModelForm):
    class Meta:
        model = Documentos
        fields = ["sri", "iess", "niv_financiero", "niv_tributario", "niv_laboral", "trabajadores"]

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["tipo", "cat_servicio"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaServicios
        fields = ["categorias"]