from django import forms
from .models import Cargo, Empleado, Tarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        
class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']