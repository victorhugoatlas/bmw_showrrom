from django.urls import path
from . import views

urlpatterns = [
    path('', views.showroom_home, name='showroom_home'),
    path('modelo/novo/', views.vehicle_create, name='vehicle_create'),
    path('modelo/<int:pk>/editar/', views.vehicle_update, name='vehicle_update'),
    path('modelo/<int:pk>/eliminar/', views.vehicle_delete, name='vehicle_delete'),
]