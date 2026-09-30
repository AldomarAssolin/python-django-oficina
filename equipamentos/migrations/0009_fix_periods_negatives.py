from django.db import migrations


def corrigir_valores_negativos(apps, schema_editor):
    # Obtém o model na versão histórica da migração
    Equipment = apps.get_model('equipamentos', 'Equipment')

    # Converte qualquer período negativo ou zerado para um valor padrão válido (ex: 30 dias)
    Equipment.objects.filter(maintenance_period__lte=0).update(maintenance_period=30)


class Migration(migrations.Migration):

    dependencies = [
        # Mantém a dependência da migração anterior
        ('equipamentos', '0008_alter_equipment_options_alter_equipment_images_and_more'), 
    ]

    operations = [
        migrations.RunPython(corrigir_valores_negativos, reverse_code=migrations.RunPython.noop),
    ]