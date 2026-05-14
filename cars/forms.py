# /app/forms.py

from django import forms
from cars.models import Brand, Car

class CarForm(forms.Form):
    brand = forms.ModelChoiceField(Brand.objects.all())
    model = forms.CharField(max_length=200)
    variation = forms.CharField(max_length=200)
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
    
    def save(self):
        car = Car(
            brand = self.cleaned_data['brand'],
            model = self.cleaned_data['model'],
            variation = self.cleaned_data['variation'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'