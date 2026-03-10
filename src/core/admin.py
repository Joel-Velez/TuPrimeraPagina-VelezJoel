from django.contrib import admin

# Register your models here.
from .models import Cargo, Empleado, Tarea

admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Tarea)