from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from cars.models import Car, Brand
from cars.forms import CarModelForm, BrandModelForm


class StaffRequiredMixin(UserPassesTestMixin):
    """Garante que apenas membros da equipe (is_staff) acessem a view."""
    def test_func(self):
        return self.request.user.is_staff


# ==========================================
# VIEWS DE CARROS
# ==========================================

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-id')
        
        search = self.request.GET.get('search')
        brand_id = self.request.GET.get('brand')
        min_year = self.request.GET.get('min_year')
        max_year = self.request.GET.get('max_year')
        location = self.request.GET.get('location')

        if search:
            queryset = queryset.filter(model__icontains=search)
        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
        if min_year:
            queryset = queryset.filter(model_year__gte=min_year)
        if max_year:
            queryset = queryset.filter(model_year__lte=max_year)
        if location:
            queryset = queryset.filter(city__icontains=location)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all().order_by('name')
        return context


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class NewCarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = reverse_lazy('cars_list')
    login_url = 'login'


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('cars_list')
    login_url = 'login'


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')
    login_url = 'login'


# ==========================================
# VIEWS DE MARCAS (STAFF/ADMIN)
# ==========================================

class BrandListView(StaffRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    ordering = ['name']


class BrandCreateView(StaffRequiredMixin, CreateView):
    model = Brand
    form_class = BrandModelForm
    template_name = 'brand_form.html'
    success_url = reverse_lazy('brand_list')


class BrandDeleteView(StaffRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_confirm_delete.html'
    success_url = reverse_lazy('brand_list')