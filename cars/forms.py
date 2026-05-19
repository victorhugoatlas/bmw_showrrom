# \cars\forms.py

from django import forms
from cars.models import Car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 15000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$215.000')
        return value
        
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1950:
            self.add_error('factory_year', 'Não é possivel cadastrar carros fabricados antes de 1950')
        return factory_year