from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'core'

urlpatterns = [
    # Home
    path('', views.index, name='index'),
    
    # Cargos:
    path('cargo/lista/', views.CargoList.as_view(), name='cargo_list'),
    path('cargo/detail/<int:pk>', views.CargoDetail.as_view(), name='cargo_detail'),
    path('cargo/create/', views.CargoCreate.as_view(), name='cargo_create'),
    path('cargo/delete/<int:pk>', views.CargoDelete.as_view(), name='cargo_delete'),
    path('cargo/update/<int:pk>', views.CargoUpdate.as_view(), name='cargo_update'),
    
    # Empleados:
    path('empleado/create/', views.EmpleadoCreate.as_view(), name='empleado_create'),
    
    # Tareas:
    path('tarea/create/', views.TareaCreate.as_view(), name='tarea_create'),
       
    # Login, Logout, Register
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),
    
]