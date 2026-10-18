from django import forms
from .models import VehicleModel

class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = [
            'family', 'title', 'subtitle', 'fuel_type', 'order',
            'is_m_model', 'image', 'pdf_file'
        ]
        labels = {
            'family': 'Família / Série',
            'title': 'Modelo e Versão',
            'subtitle': 'Código (ex: G30, F30, U11...)',
            'fuel_type': 'Motorização',
            'order': 'Ordem de Exibição (Ex: 1, 2, 3...)',
            'is_m_model': 'Modelo M ou M Performance',
            'image': 'Imagem do Veículo',
            'pdf_file': 'Ficheiro PDF do Configurador',
        }
        widgets = {
            'family': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'placeholder': 'Ex: 320i M Sport ou X1 sDrive20i'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'placeholder': 'Ex: G20, G30, U11'
            }),
            'fuel_type': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'order': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black',
                'min': '1'
            }),
            'is_m_model': forms.CheckboxInput(attrs={
                'class': 'w-4 h-4 text-black border-gray-300 rounded focus:ring-black'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
            'pdf_file': forms.FileInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-black bg-white'
            }),
        }