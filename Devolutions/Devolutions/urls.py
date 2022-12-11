
from django.contrib import admin
from django.urls import path, include
from Devolu.views import registrarse, registrar, listadev, registrard,registrardevo, eliminardev, devoluActualizar, editarDev,menu

urlpatterns = [
    path('inicio/', include('django.contrib.auth.urls')),
    path('registrarse/', registrar),
    path('registrarse/', registrarse),
    path('admin/', admin.site.urls),
    path('lista/',listadev),
    path('registrodev/', registrard),
    path('registrardevolucio/', registrardevo),
    path('eliminar/<id>',eliminardev),
    path('actualizar/<id>', devoluActualizar),
    path('editardevo/', editarDev),
    path('menu/', menu)
]
