from django.contrib import admin
from . import models as m

# Register your models here.
admin.site.register(m.DCliente)
admin.site.register(m.Devolucion)