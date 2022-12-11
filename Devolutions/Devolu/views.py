from django.shortcuts import render, redirect
from Devolu.models import DCliente, AdminUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


def registrarse(request):
    cli_username = request.POST['txt_username']
    cli_email = request.POST['txt_email']
    cli_password = request.POST['txt_contrasena']
    cli_nombre =request.POST['txt_nombres']
    cli_apellido = request.POST['txt_apellidos']
    cli_rut = request.POST['txt_rut']
    cli_celular = request.POST['txt_celular']

    user = AdminUser(username=cli_username, rut = cli_rut, nombre = cli_nombre, apellido = cli_apellido, email = cli_email, celular = cli_celular)
    user.set_password(cli_password)
    user.save()
    grupo, created = Group.objects.get_or_create(name ='admin')
    user.groups.add(grupo)

    return redirect('/inicio/login/')

def registrar(request):
    if request.user.is_authenticated:
        redirect('/menu/')
    return render(request,'registrarse.html')

@login_required
def listadev(request):
    dcliente = DCliente.objects.all()
    data = {'dcliente':dcliente}
    return render(request,'listarDevolucion.html', data)

@login_required
def registrard(request):
    return render(request,'FormularioDev.html')    

@login_required
def registrardevo(request):
    dev_rut = request.POST['txt_rut']
    dev_nombre = request.POST['txt_nombre']
    dev_apellido = request.POST['txt_apellido']
    dev_email = request.POST['txt_email']
    dev_celular = request.POST['txt_celular']
    dev_cantidad = request.POST['txt_cantidad']
    dev_producto  = request.POST['txt_producto']
    dev_codigo = request.POST['txt_codigo']
    dev_nombreV = request.POST['txt_nombrevendedor']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_comentario = request.POST['txt_comentario']

    devolucion = DCliente(rut = dev_rut, nombre = dev_nombre, apellido = dev_apellido, email = dev_email, celular = dev_celular, cantidad = dev_cantidad, producto = dev_producto, codigo = dev_codigo, nombrevendedor = dev_nombreV, distribuidor = dev_distribuidor, comentario = dev_comentario)

    devolucion.save()

    return redirect('/')


@login_required
def eliminardev(request, id):
    elemidev = DCliente.objects.get(id=id)
    elemidev.delete()

    return redirect('/')

login_required
def devoluActualizar(request,id):
    dev = DCliente.objects.get(id=id)
    return render(request,'Actualizardev.html',{"dev":dev})    

@login_required
def editarDev(request):
    dev_rut = request.POST['txt_rut']
    dev_nombre = request.POST['txt_nombre']
    dev_apellido = request.POST['txt_apellido']
    dev_email = request.POST['txt_email']
    dev_celular = request.POST['txt_celular']
    dev_cantidad = request.POST['txt_cantidad']
    dev_producto  = request.POST['txt_producto']
    dev_codigo = request.POST['txt_codigo']
    dev_nombreV = request.POST['txt_nombrevendedor']
    dev_distribuidor = request.POST['txt_distribuidor']
    dev_comentario = request.POST['txt_comentario']

    devolu = DCliente.objects.get(rut = dev_rut)

    devolu.nombre = dev_nombre
    devolu.apellido = dev_apellido
    devolu.email = dev_email
    devolu.celular = dev_celular
    devolu.cantidad = dev_cantidad
    devolu.producto = dev_producto
    devolu.codigo = dev_codigo
    devolu.nombrevendedor = dev_nombreV
    devolu.distribuidor = dev_distribuidor
    devolu.comentario = dev_comentario

    devolu.save()
    return redirect('/')


@login_required
def menu(request):
    return render(request,'menu.html')     