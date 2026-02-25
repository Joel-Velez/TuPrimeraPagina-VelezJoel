from django.db import models

# Create your models here.


class Cargo(models.Model):
    cargo = models.CharField(max_length=250)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.cargo
    
    

class Empleado(models.Model):
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    fecha_de_ingreso = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido
    
    
    
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre