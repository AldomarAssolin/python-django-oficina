from django.db import models

class Equipment(models.Model):

    """gestão de ativos e equipamentos para controle operacional de chão de fábrica"""

    class StatusOptions(models.TextChoices):
        ATIVO = 'ATIVO', 'Ativo / Operacional'
        MANUTENCAO = 'MANUTENCAO' , 'Em Manutenção'
        INATIVO = 'INATIVO', 'Inativo / Desativado'

    name = models.CharField(verbose_name="Nome",max_length=150,)
    id_code = models.CharField(verbose_name="Código de Identificação",max_length=20, unique=True, default="EQP-XXX")
    brand = models.CharField(verbose_name="Marca",max_length=100,)
    manufacturer = models.CharField(verbose_name="Fabricante",max_length=50,)
    model = models.CharField(verbose_name="Modelo",max_length=100,)
    serial_number = models.CharField(verbose_name="Número de Série",max_length=100, unique=True, )
    purchase_date = models.DateField(verbose_name="Data Compra",blank=False, null=False)
    purchase_value = models.DecimalField(verbose_name="Valor Compra",max_digits=10, decimal_places=2,)

    status = models.CharField(
        verbose_name="Situação",
        max_length=50,
        choices=StatusOptions.choices,
        default=StatusOptions.ATIVO
        )

    maintenance_period = models.IntegerField(verbose_name="Período de Manutenção",blank=False, null=False)
    last_maintenance_date = models.DateField(verbose_name="Última Manutenção",blank=False, null=False)
    notes = models.CharField(verbose_name="Descição/Observação",max_length=250,)
    created_at = models.DateTimeField(verbose_name="Data Cadastro", auto_now_add=True)

    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"

    def __str__(self) -> str:
        return f"{self.name} / {self.status}"