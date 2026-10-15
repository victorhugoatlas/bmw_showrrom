from django import forms
from cars.models import Car, Brand


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'w-full bg-zinc-800 text-white border border-zinc-700 rounded-lg px-4 py-2.5 focus:outline-none focus:border-pink-500 focus:ring-1 focus:ring-pink-500 transition-colors'
                })
            else:
                field.widget.attrs.update({
                    'class': 'w-5 h-5 accent-pink-600 rounded bg-zinc-800 border-zinc-700'
                })


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-zinc-800 text-white border border-cyan-500/40 rounded-lg px-4 py-2.5 focus:outline-none focus:border-pink-500 focus:ring-1 focus:ring-pink-500 transition-colors',
                'placeholder': 'Ex: BMW, Porsche, Volkswagen'
            })
        }