import datetime
from django.db import models

class Equipment(models.Model):

    """gestão de ativos e equipamentos para controle operacional de chão de fábrica"""

    class StatusOptions(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo / Operacional'
        MANUTENCAO = 'MANUTENCAO' , 'Em Manutenção'
        INATIVO = 'INATIVO', 'Inativo / Desativado'

    name = models.CharField(verbose_name="Nome",max_length=150)
    id_code = models.CharField(verbose_name="Código de Identificação",max_length=20, unique=True)
    brand = models.CharField(verbose_name="Marca",max_length=100)
    manufacturer = models.CharField(verbose_name="Fabricante",max_length=50)
    model = models.CharField(verbose_name="Modelo",max_length=100)
    serial_number = models.CharField(verbose_name="Número de Série", max_length=50)
    purchase_date = models.DateField(verbose_name="Data Compra")
    purchase_value = models.DecimalField(verbose_name="Valor Compra",max_digits=10, decimal_places=2,)

    status = models.CharField(
        verbose_name="Situação",
        max_length=20,
        choices=StatusOptions.choices,
        default=StatusOptions.ATIVO
        )

    maintenance_period = models.PositiveIntegerField(verbose_name="Periodicidade de Manutenção (Dias)")
    last_maintenance_date = models.DateField(verbose_name="Última Manutenção")
    notes = models.TextField(verbose_name="Descição/Observação", blank=True, null=True)
    images = models.ImageField(verbose_name="Imagens",upload_to='equipments/%Y/%m', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Data Cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        """Higieniza o id_code para caixa alta antes de salvar."""

        if self.id_code:
            self.id_code = self.id_code.strip().upper()

        super().save(*args, **kwargs)

    @property
    def next_maintenance(self):
        """Calcula a data da próxima manutenção preventiva."""
        if self.last_maintenance_date and self.maintenance_period:
            return self.last_maintenance_date + datetime.timedelta(days=self.maintenance_period)
        return None

    def __str__(self) -> str:
        return f"{self.id_code} - {self.name} ({self.get_status_display()})"