from django.shortcuts import render

from equipamentos.models import Equipment



def equipaments_views(request):
    # Otimização ORM: Carrega apenas os campos necessários para a listagem
    equipaments = Equipment.objects.all().only(
        'id_code', 'name', 'brand', 'model', 'status', 'last_maintenance_date', 'images'
    )

    context = {
        'equipaments': equipaments,
        'total_equipamentos': equipaments.count(),
        'total_ativos': equipaments.filter(status=Equipment.StatusOptions.ATIVO).count(),
    }

    return render(
        request,
        'equipamentos.html',
        context
    )

