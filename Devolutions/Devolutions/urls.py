"""Devolutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from Devolu.views import registrarse, listadev, registrard,registrardevo, eliminardev, devoluActualizar, editarDev, registrar,menu, crearVend

urlpatterns = [
    path('inicio/', include('django.contrib.auth.urls')),
    path('registrarse/', registrarse),
    path('admin/', admin.site.urls),
    path('lista/',listadev),
    path('registrodev', registrard),
    path('registrardevolucio/', registrardevo),
    path('eliminar/<id>',eliminardev),
    path('actualizar/<id>', devoluActualizar),
    path('editardevo/', editarDev),
    path('registrar/', registrar),
    path('menu/',menu),
    path('crearuser/', crearVend)

]
