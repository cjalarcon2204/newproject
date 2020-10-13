from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .forms import UserCreationForm, RolForm, RolUsuarioForm
from .models import User, Rol, RolUsuario
# Create your views here.
def login(request, plantilla="login/login.html"):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuarios
            user = authenticate(username=username, password=password)

            # Si existe un usuarios con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect("inicio")



    # Si llegamos al final renderizamos el formulario
    return render(request, plantilla, {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect("login")

@login_required(login_url='/')
def inicio(request):
    return render(request, "base.html")

#Crud de usuarios , roles y rolesusuarios
def consultarusuarios(request, plantilla="usuarios/consultarusuarios.html"):
    usuarios = User.objects.all
    return render(request, plantilla, {'usuarios':usuarios})

def consultarroles(request, plantilla="usuarios/consultarroles.html"):
    roles = Rol.objects.all
    return render(request, plantilla, {'roles':roles})

def consultarrolesusuarios(request, plantilla="usuarios/consultarrolesusuarios.html"):
    rolesusuarios = RolUsuario.objects.all
    return render(request, plantilla, {'rolesusuarios':rolesusuarios})

def crearusuario(request, plantilla="usuarios/crearusuario.html"):
    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('consultar_usuarios')
    else:
        form=UserCreationForm()
    return render(request, plantilla, {'UserCreationForm':form})

def crearrol(request, plantilla="usuarios/crearrol.html"):
    if request.method=="POST":
        form = RolForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles')
    else:
        form=RolForm()
    return render(request, plantilla, {'RolForm':form})

def crearrolusuario(request, plantilla="usuarios/crearrolusuario.html"):
    if request.method=="POST":
        formRolUsuario = RolUsuarioForm(request.POST or None)
        if formRolUsuario.is_valid():
            formRolUsuario.save()
        return redirect('consultar_roles_usuarios')
    else:
        formRolUsuario=RolUsuarioForm()
    return render(request, plantilla, {'formRolUsuario':formRolUsuario})

def modificarusuario(request, id, plantilla="usuarios/modificarusuario.html"):
    usuario = User.objects.get(id = id)
    if request.method=="GET":
        form = UserCreationForm(request.POST or None, instance=usuario)
    else:
        form = UserCreationForm(request.POST or None, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('consultar_usuarios')
    return render(request, plantilla, {'form':form})

def modificarrol(request, id, plantilla="usuarios/modificarrol.html"):
    rol = Rol.objects.get(id = id)
    if request.method=="GET":
        form = RolForm(request.POST or None, instance=rol)
    else:
        form = RolForm(request.POST or None, instance=rol)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles')
    return render(request, plantilla, {'form':form})

def modificarrolusuario(request, id, plantilla="usuarios/modificarrolusuario.html"):
    rolusuario = RolUsuario.objects.get(id = id)
    if request.method=="GET":
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
    else:
        form = RolUsuarioForm(request.POST or None, instance=rolusuario)
        if form.is_valid():
            form.save()
        return redirect('consultar_roles_usuarios')
    return render(request, plantilla, {'form':form})


def eliminarusuario(request, id, plantilla="usuarios/eliminarusuario.html"):
    usuario = User.objects.get(id = id)
    if request.method=="GET":
        usuario.delete()
        return redirect('consultar_usuarios')
    return render(request, plantilla, {'usuarios':usuario})

def eliminarrol(request, id, plantilla="usuarios/eliminarrol.html"):
    rol = Rol.objects.get(id = id)
    if request.method=="GET":
        rol.delete()
        return redirect('consultar_roles')
    return render(request, plantilla, {'rol':rol})

def eliminarrolusuario(request, id, plantilla="usuarios/eliminarrolusuario.html"):
    rolusuario = RolUsuario.objects.get(id = id)
    if request.method=="POST":
        rolusuario.delete()
        return redirect('consultar_roles_usuarios')
    return render(request, plantilla, {'rolusuario':rolusuario})