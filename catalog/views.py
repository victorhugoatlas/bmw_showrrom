from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import VehicleModel
from .forms import VehicleModelForm

def showroom_home(request):
    # Ordem personalizada das séries
    custom_order = ['X7', 'X6', 'X5', 'X4', 'X3', 'X2', 'X1', '7', '6', '5', '4', '3', '2', '1', 'Z']
    
    all_vehicles = VehicleModel.objects.all()
    
    # Ordenar veículos com base na ordem exata solicitada
    vehicles = sorted(
        all_vehicles, 
        key=lambda v: custom_order.index(v.family) if v.family in custom_order else 99
    )

    active_family_codes = set(v.family for v in vehicles)
    
    families_filter = []
    for code in custom_order:
        if code in active_family_codes:
            display_name = dict(VehicleModel.FAMILY_CHOICES).get(code, code)
            families_filter.append({'code': code, 'name': display_name})

    context = {
        'vehicles': vehicles,
        'families_filter': families_filter,
    }
    return render(request, 'catalog/index.html', context)


@login_required
def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo cadastrado com sucesso!')
            return redirect('showroom_home')
    else:
        form = VehicleModelForm()
    
    return render(request, 'catalog/vehicle_form.html', {'form': form, 'title': 'Cadastrar Modelo'})


@login_required
def vehicle_update(request, pk):
    vehicle = get_object_or_404(VehicleModel, pk=pk)
    if request.method == 'POST':
        form = VehicleModelForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Modelo atualizado com sucesso!')
            return redirect('showroom_home')
    else:
        form = VehicleModelForm(instance=vehicle)
    
    return render(request, 'catalog/vehicle_form.html', {'form': form, 'title': f'Editar Modelo: {vehicle.title}'})


@login_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(VehicleModel, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        messages.success(request, 'Modelo eliminado com sucesso!')
        return redirect('showroom_home')
    
    return render(request, 'catalog/confirm_delete.html', {
        'object': vehicle,
        'title': f'Eliminar Modelo: {vehicle.title}'
    })