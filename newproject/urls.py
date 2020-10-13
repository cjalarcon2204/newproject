"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuario.views import *
from perfil_empresa.views import *
from usuario.views import *

urlpatterns = [

    #cliente
    path("registrar-cliente/", crear_cliente, name="registrar_cliente"),
    path("modificar-cliente/<int:id>", editar_cliente, name="modificar_cliente"),
    path("eliminar-cliente/<int:id>", eliminar_cliente, name="eliminar_cliente"),
    path("consultar-cliente/", consultar_cliente, name="consultar_cliente"),

    #documentos
    path("registrar-documentos/", crear_documentos, name="registrar_documentos"),
    path("modificar-documentos/<int:id>", editar_documentos, name="modificar_documentos"),
    path("eliminar-documentos/<int:id>", eliminar_documentos, name="eliminar_documentos"),
    path("consultar-documentos/", consultar_documentos, name="consultar_documentos"),

    #empresa
    path("registrar-empresa/", crear_empresa, name="registrar_empresa"),
    path("modificar-empresa/<int:id>", editar_empresa, name="modificar_empresa"),
    path("eliminar-empresa/<int:id>", eliminar_empresa, name="eliminar_empresa"),
    path("consultar-empresa/", consultar_empresa, name="consultar_empresa"),

    #SERVICIOS
    path("registrar-servicio/", crear_servicio, name="registrar_servicio"),
    path("modificar-servicio/<int:id>", editar_servicio, name="modificar_servicio"),
    path("eliminar-servicio/<int:id>", eliminar_servicio, name ="eliminar_servicio"),
    path("consultar-servicio/", consultar_servicio, name="consultar_servicio"),

    # CATEGORIA SERVICIOS
    path("registrar-categoria/", crear_categoria, name="registrar_categoria"),
    path("modificar-categoria/<int:id>", editar_categoria, name="modificar_categoria"),
    path("eliminar-categoria/<int:id>", eliminar_categoria, name="eliminar_categoria"),
    path("consultar-categoria/", consultar_categoria, name="consultar_categoria"),

    #usuarios
    path('consultar_usuarios/', consultarusuarios, name="consultar_usuarios"),
    path('crear_usuario/', crearusuario, name="crear_usuario"),
    path('modificar_usuario/<int:id>', modificarusuario, name="modificar_usuario"),
    path('eliminar_usuario/<int:id>', eliminarusuario, name="eliminar_usuario"),

    #roles
    path('consultar_roles/', consultarroles, name="consultar_roles"),
    path('crear_rol/', crearrol, name="crear_rol"),
    path('modificar_rol/<int:id>', modificarrol, name="modificar_rol"),
    path('eliminar_rol/<int:id>', eliminarrol, name="eliminar_rol"),

    # roles y usuarios relacionados
    path('consultar_roles_usuarios/', consultarrolesusuarios, name="consultar_roles_usuarios"),
    path('crear_rol_usuario/', crearrolusuario, name="crear_rol_usuario"),
    path('modificar_rol_usuario/<int:id>', modificarrolusuario, name="modificar_rol_usuario"),
    path('eliminar_rol_usuario/<int:id>', eliminarrolusuario, name="eliminar_rol_usuario"),

    #login y logout
    path("", login, name="login"),
    path("logout/", logout, name="logout" ),
    path("inicio/", inicio, name="inicio"),
    path('admin/', admin.site.urls),
]
