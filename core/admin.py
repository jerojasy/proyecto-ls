from django.contrib import admin
from core.models import *

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['usuario','fecha_reserva', 'hora_reserva', 'estado', 'especialidad']
    list_filter = ['fecha_reserva']
    search_fields = ['fecha_reserva', 'estado', 'especialidad']


admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Proveedor)
admin.site.register(Especialidad)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Producto)