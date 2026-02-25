from django import forms
from .models import Cargo, Empleado, Tarea

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'