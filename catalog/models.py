from django.db import models

class VehicleModel(models.Model):
    FAMILY_CHOICES = [
        ('X7', 'X7'),
        ('X6', 'X6'),
        ('X5', 'X5'),
        ('X4', 'X4'),
        ('X3', 'X3'),
        ('X2', 'X2'),
        ('X1', 'X1'),
        ('7', 'Série 7'),
        ('6', 'Série 6'),
        ('5', 'Série 5'),
        ('4', 'Série 4'),
        ('3', 'Série 3'),
        ('2', 'Série 2'),
        ('1', 'Série 1'),
        ('Z', 'Z'),
    ]

    FUEL_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('flex', 'Flex'),
        ('phev', 'Híbrido Plug-In'),
        ('eletrico', 'Elétrico'),
        ('diesel', 'Diesel'),
    ]

    family = models.CharField(
        max_length=10, 
        choices=FAMILY_CHOICES, 
        verbose_name="Família / Série",
        help_text="Usado para o filtro e ordenação inicial"
    )
    title = models.CharField(
        max_length=100, 
        verbose_name="Modelo e Versão", 
        help_text="Ex: 320i M Sport, X1 sDrive20i"
    )
    subtitle = models.CharField(
        max_length=50, 
        blank=True,
        null=True,
        verbose_name="Código", 
        help_text="Código da geração/chassi (Ex: G30, F30, U11...)"
    )
    fuel_type = models.CharField(
        max_length=50, 
        choices=FUEL_CHOICES, 
        default='gasolina', 
        verbose_name="Motorização"
    )
    order = models.PositiveIntegerField(
        default=1,
        verbose_name="Ordem de Exibição",
        help_text="Número para ordenar modelos dentro da mesma série (Ex: 1, 2, 3...)"
    )
    
    is_m_model = models.BooleanField(default=False, verbose_name="Modelo M ou M Performance")
    
    image = models.ImageField(upload_to='bmw_vehicles/', verbose_name="Imagem do Veículo")
    pdf_file = models.FileField(
        upload_to='bmw_pdfs/', 
        blank=True, 
        null=True, 
        verbose_name="Ficheiro PDF do Configurador"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Modelo de Veículo"
        verbose_name_plural = "Modelos de Veículos"
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.get_family_display()} - {self.title}"