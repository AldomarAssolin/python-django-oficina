from django.shortcuts import render

from equipamentos.models import Equipment



def equipments_views(request):
    # Otimização ORM: Carrega apenas os campos necessários para a listagem
    equipments = Equipment.objects.all().only(
        'id_code', 
        'name', 
        'brand', 
        'model', 
        'status', 
        'last_maintenance_date', 
        'images'
    )

    context = {
        'equipments': equipments,
        'total_equipamentos': equipments.count(),
        'total_ativos': equipments.filter(status=Equipment.StatusOptions.ATIVO).count(),
    }

    return render(
        request,
        'equipamentos.html',
        context
    )

