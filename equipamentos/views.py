from django.shortcuts import render, get_object_or_404

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


def equipment_detail_view(request,id_code):
    # Busca o equipamento pelo código de identificação (id_code)
    equipment = get_object_or_404(Equipment, id_code=id_code)

    context = {
        'equipment': equipment,
    }

    return render(
        request,
        'equipamentos/detail.html',
        context
    )
