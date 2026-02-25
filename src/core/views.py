# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models
from . import forms
from django.urls import reverse_lazy

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
    
    
    
class EmpleadoCreate(CreateView):
    model = models.Cargo
    form_class = forms.CargoForm
    success_url = reverse_lazy('core:cargo_list')
    
class TareaCreate(CreateView):
    model = models.Tarea
    form_class = forms.CargoForm
    success_url = reverse_lazy('core:cargo_list')