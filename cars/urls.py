from django.urls import path
from cars.views import (
    CarsListView, NewCarCreateView, CarDetailView, CarUpdateView, CarDeleteView,
    BrandListView, BrandCreateView, BrandDeleteView
)

urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    
    # Painel de Gerenciamento de Marcas (Staff/Admin)
    path('brands/', BrandListView.as_view(), name='brand_list'),
    path('brands/new/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),
]