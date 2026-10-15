from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Marca")

    def __str__(self):
        return self.name


class Car(models.Model):
    GEAR_CHOICES = (
        ('AT', 'Automática'),
        ('MT', 'Manual'),
        ('CVT', 'CVT'),
        ('DCT', 'Dupla Embreagem'),
    )

    FUEL_CHOICES = (
        ('FLEX', 'Gasolina e álcool'),
        ('GAS', 'Gasolina'),
        ('ETH', 'Etanol'),
        ('DIE', 'Diesel'),
        ('ELE', 'Elétrico'),
        ('HYB', 'Híbrido'),
    )

    BODY_CHOICES = (
        ('SED', 'Sedã'),
        ('SUV', 'SUV'),
        ('HAT', 'Hatchback'),
        ('COU', 'Cupê'),
        ('PIC', 'Picape'),
        ('CON', 'Conversível'),
    )

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand', verbose_name="Marca", null=True, blank=True)
    model = models.CharField(max_length=200, verbose_name="Modelo")
    version = models.CharField(max_length=200, verbose_name="Versão", default="1.0")
    
    city = models.CharField(max_length=100, verbose_name="Cidade", default="São Paulo")
    state = models.CharField(max_length=2, verbose_name="Estado (UF)", default="SP")
    
    factory_year = models.IntegerField(verbose_name="Ano Fabricação", default=2020)
    model_year = models.IntegerField(verbose_name="Ano Modelo", default=2020)
    km = models.IntegerField(verbose_name="Quilometragem (KM)", default=0)
    
    gear = models.CharField(max_length=3, choices=GEAR_CHOICES, verbose_name="Câmbio", default='AT')
    fuel = models.CharField(max_length=4, choices=FUEL_CHOICES, verbose_name="Combustível", default='FLEX')
    body_type = models.CharField(max_length=3, choices=BODY_CHOICES, verbose_name="Carroceria", default='SED')
    color = models.CharField(max_length=50, verbose_name="Cor", default="Preto")
    plate_end = models.IntegerField(verbose_name="Final da Placa", default=0)
    accepts_trade = models.BooleanField(default=False, verbose_name="Aceita Troca")
    
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor (R$)", default=0.00)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True, verbose_name="Foto Principal")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição Adicional")

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ['-id']

    def __str__(self):
        brand_name = self.brand.name if self.brand else "Sem Marca"
        return f"{brand_name} {self.model} {self.version}"