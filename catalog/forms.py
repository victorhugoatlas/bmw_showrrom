from django import forms
from .models import VehicleModel

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = [
            'family', 'title', 'subtitle', 'fuel_type',
            'is_m_model', 'image', 'configurator_url', 'pdf_file'
        ]
        labels = {
            'family': 'Família / Série',
            'title': 'Modelo e Versão',
            'subtitle': 'Código (ex: G30, F30, G20...)',
            'fuel_type': 'Motorização',
            'is_m_model': 'Modelo M ou M Performance',
            'image': 'Imagem do Veículo',
            'configurator_url': 'Link do Configurador Alemão',
            'pdf_file': 'Ficheiro PDF do Configurador',
        }
        widgets = {
            'family': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'placeholder': 'Ex: 320i M Sport ou X7 xDrive40i'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'placeholder': 'Ex: G20, G30, F30'
            }),
            'fuel_type': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'is_m_model': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-black border-gray-300 rounded focus:ring-black'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'configurator_url': forms.URLInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'placeholder': 'https://configurator.bmw.de/...'
            }),
            'pdf_file': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
        }