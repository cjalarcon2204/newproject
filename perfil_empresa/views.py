from django.shortcuts import render, redirect
from .forms import EmpresaForm, ClienteForm, DocumentosForm, ServicioForm, CategoriaForm
from .models import Empresa, Cliente, Documentos, Servicio, CategoriaServicios

# CRUD de Cliente
def consultar_cliente(request, plantilla="clientes/consultar.html"):
    cliente_obj = Cliente.objects.all()
    return render(request, plantilla, {'cliente_obj': cliente_obj})

def crear_cliente(request, plantilla='clientes/registrar.html'):
    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('consultar_cliente')
    else:
        form = ClienteForm()
    return render(request, plantilla, {'ClienteForm':form})


def editar_cliente(request,id,plantilla='clientes/editar.html'):
    cliente_obj = Cliente.objects.get(id = id)
    if request.method == 'GET':
        form = ClienteForm(request.POST or None, instance = cliente_obj)
    else:
        form = ClienteForm(request.POST or None, instance = cliente_obj)
        if form.is_valid():
            form.save()
            return redirect('consultar_cliente')
    return render(request, plantilla, {'ClienteForm':form})


def eliminar_cliente(request, id, plantilla = 'clientes/eliminar.html'):
    cliente_obj = Cliente.objects.get(id = id)
    if request.method == 'GET':
        Cliente.delete(Cliente.objects.get(id = id))
        return redirect('consultar_cliente')
    return render(request, plantilla,{'cliente_obj':cliente_obj})




# CRUD de Empresa
def consultar_empresa(request, plantilla="empresa/consultar.html"):
    empresa_obj = Empresa.objects.all()
    return render(request, plantilla, {'empresa_obj': empresa_obj})

def crear_empresa(request, plantilla='empresa/registrar.html'):
    if request.method == 'POST':
        form = EmpresaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('consultar_empresa')
    else:
        form = EmpresaForm()
    return render(request, plantilla, {'EmpresaForm':form})


def editar_empresa(request,id,plantilla='empresa/editar.html'):
    empresa_obj = Empresa.objects.get(id = id)
    if request.method == 'GET':
        form = EmpresaForm(request.POST or None, request.FILES or None, instance = empresa_obj)
    else:
        form = EmpresaForm(request.POST or None, request.FILES or None, instance = empresa_obj)
        if form.is_valid():
            form.save()
            return redirect('consultar_empresa')
    return render(request, plantilla, {'EmpresaForm':form})


def eliminar_empresa(request, id, plantilla = 'empresa/eliminar.html'):
    empresa_obj = Empresa.objects.get(id = id)
    if request.method == 'GET':
        Empresa.delete(Empresa.objects.get(id = id))
        return redirect('consultar_empresa')
    return render(request, plantilla,{'empresa_obj':empresa_obj})




# CRUD de Documentos
def consultar_documentos(request, plantilla="documentos/consultar.html"):
    documentos_obj = Documentos.objects.all()
    return render(request, plantilla, {'documentos_obj': documentos_obj})

def crear_documentos(request, plantilla='documentos/registrar.html'):
    if request.method == 'POST':
        form = DocumentosForm(request.POST or None, request.FILES or None )
        if form.is_valid():
            form.save()
            return redirect('consultar_documentos')
    else:
        form = DocumentosForm()
    return render(request, plantilla, {'DocumentosForm':form})


def editar_documentos(request,id,plantilla='documentos/editar.html'):
    documentos_obj = Documentos.objects.get(id = id)
    if request.method == 'GET':
        form = DocumentosForm(request.POST or None, request.FILES or None, instance = documentos_obj)
    else:
        form = DocumentosForm(request.POST or None, request.FILES or None, instance = documentos_obj)
        if form.is_valid():
            form.save()
            return redirect('consultar_documentos')
    return render(request, plantilla, {'DocumentosForm':form})


def eliminar_documentos(request, id, plantilla = 'documentos/eliminar.html'):
    documentos_obj = Documentos.objects.get(id = id)
    if request.method == 'GET':
        Documentos.delete(Documentos.objects.get(id = id))
        return redirect('consultar_documentos')
    return render(request, plantilla,{'documentos_obj':documentos_obj})



#CRUD SERVICIO
def consultar_servicio(request, plantilla="servicio/consultar.html"):
    servicio_obj = Servicio.objects.all()
    return render(request, plantilla, {'servicio_obj': servicio_obj})

def crear_servicio(request, plantilla='servicio/registrar.html'):
    if request.method == 'POST':
        form = ServicioForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('consultar_servicio')
    else:
        form = ServicioForm()
    return render(request, plantilla, {'ServicioForm':form})


def editar_servicio(request,id,plantilla='servicio/editar.html'):
    servicio_obj = Servicio.objects.get(id = id)
    if request.method == 'GET':
        form = ServicioForm(request.POST or None, instance = servicio_obj)
    else:
        form = ServicioForm(request.POST or None, instance = servicio_obj)
        if form.is_valid():
            form.save()
            return redirect('consultar_servicio')
    return render(request, plantilla, {'ServicioForm':form})


def eliminar_servicio(request, id, plantilla = 'servicio/eliminar.html'):
    servicio_obj = Servicio.objects.get(id = id)
    if request.method == 'GET':
        Servicio.delete(Servicio.objects.get(id = id))
        return redirect('consultar_documentos')
    return render(request, plantilla,{'servicio_obj':servicio_obj})



#CRUD CATEGORIA SERVICIO
def consultar_categoria(request, plantilla="categoria/consultar.html"):
    categoria_obj = CategoriaServicios.objects.all()
    return render(request, plantilla, {'categoria_obj': categoria_obj})

def crear_categoria(request, plantilla='categoria/registrar.html'):
    if request.method == 'POST':
        form = CategoriaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('consultar_categoria')
    else:
        form = CategoriaForm()
    return render(request, plantilla, {'CategoriaForm':form})


def editar_categoria(request,id,plantilla='categoria/editar.html'):
    categoria_obj = CategoriaServicios.objects.get(id = id)
    if request.method == 'GET':
        form = CategoriaForm(request.POST or None, instance = categoria_obj)
    else:
        form = CategoriaForm(request.POST or None, instance = categoria_obj)
        if form.is_valid():
            form.save()
            return redirect('consultar_categoria')
    return render(request, plantilla, {'CategoriaForm':form})


def eliminar_categoria(request, id, plantilla = 'categoria/eliminar.html'):
    categoria_obj = CategoriaServicios.objects.get(id = id)
    if request.method == 'GET':
        CategoriaServicios.delete(CategoriaServicios.objects.get(id = id))
        return redirect('consultar_categoria')
    return render(request, plantilla,{'categoria_obj':categoria_obj})