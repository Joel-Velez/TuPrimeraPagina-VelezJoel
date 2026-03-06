
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from . import forms
from django.urls import reverse_lazy
from .forms import RegisterForm


# Home
def index(request):
    return render(request, "core/index.html", {"titulo": "Mi Primera Pagina - Velez Joel"})


# Cargos
class CargoList(ListView):
    model = models.Cargo
    
    def get_queryset(self):
        consulta = self.request.GET.get('consulta')
        if consulta:
            cargo = models.Cargo.objects.filter(cargo__icontains=consulta)
        else:
            cargo = models.Cargo.objects.all()
        return cargo
    
class CargoDetail(DetailView):
    model = models.Cargo
    
class CargoCreate(CreateView):
    model = models.Cargo
    form_class = forms.CargoForm
    success_url = reverse_lazy('core:cargo_list')
    
class CargoDelete(DeleteView):
    model = models.Cargo
    success_url = reverse_lazy('core:cargo_list')
    
class CargoUpdate(UpdateView):
    model = models.Cargo
    form_class = forms.CargoForm
    success_url = reverse_lazy('core:cargo_list')
    
    
# Empleados
class EmpleadoCreate(CreateView):
    model = models.Cargo
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy('core:empleado_list')
    
class EmpleadoList(ListView):
    model = models.Empleado
    
    def get_queryset(self):
        consulta = self.request.GET.get('consulta')
        if consulta:
            empleado = models.Empleado.objects.filter(nombre__icontains=consulta)
        else:
            empleado = models.Empleado.objects.all()
        return empleado
    
class EmpleadoDetail(DetailView):
    model = models.Empleado
    
class EmpleadoUpdate(UpdateView):
    model = models.Empleado
    form_class = forms.EmpleadoForm
    success_url = reverse_lazy('core:empleado_list')
    
class EmpleadoDelete(DeleteView):
    model = models.Empleado
    success_url = reverse_lazy('core:empleado_list')
    

    
# Tareas
class TareaCreate(CreateView):
    model = models.Tarea
    form_class = forms.TareaForm
    success_url = reverse_lazy('core:tarea_list')
    
class TareaList(ListView):
    model = models.Tarea
    
    def get_queryset(self):
        consulta = self.request.GET.get('consulta')
        if consulta:
            tarea = models.Tarea.objects.filter(nombre__icontains=consulta)
        else:
            tarea = models.Tarea.objects.all()
        return tarea
    
class TareaDetail(DetailView):
    model = models.Tarea
    
class TareaUpdate(UpdateView):
    model = models.Tarea
    form_class = forms.TareaForm
    success_url = reverse_lazy('core:tarea_list')
    
class TareaDelete(DeleteView):
    model = models.Tarea
    success_url = reverse_lazy('core:tarea_list')
    

    
# Login, Logout, Register
class Register(CreateView):
    form_class = RegisterForm
    template_name = 'core/register.html'
    success_url = reverse_lazy('core:login') 
    
    
# Sobre Mi
def about(request):
    return render(request, "core/about.html", {"titulo": "Sobre Mi"})   