from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cargo/lista/', views.CargoList.as_view(), name='cargo_list'),
    # path('cargo/detail/<', views.CargoDetail.as_view(), name='cargo_detail'),
    # path('cargo/create/', views.CargoCreate.as_view(), name='cargo_create'),
    # path('cargo/delete/', views.CargoDelete.as_view(), name='cargo_delete'),
    # path('cargo/update/', views.CargoUpdate.as_view(), name='cargo_update'),
    # path('empleado/create/', views.EmpleadoCreate.as_view(), name='empleado_create'),
    # path('tarea/create/', views.TareaCreate.as_view(), name='tarea_create'),
]