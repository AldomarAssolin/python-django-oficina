from django.test import TestCase
from django.urls import reverse
from equipamentos.models import Equipment

# Helper function to create an Equipment instance for testing
def create_equipment(
        name,
        id_code,
        serial_number,
        status=Equipment.StatusOptions.ATIVO,
):
    return Equipment.objects.create(
        name=name,
        id_code=id_code,
        brand="Test Brand",
        manufacturer="Test Manufacturer",
        model="Test Model",
        serial_number=serial_number,
        purchase_date="2026-01-01",
        purchase_value=1000.00,
        status=status,
        maintenance_period=30,
        last_maintenance_date="2026-01-01"
    )

class EquipmentModelTest(TestCase):

    def setUp(self):
        """
        Testes unitários para o modelo Equipment.
        Prepara a URL e cria um equipamento de teste.
        """

        self.equipment = create_equipment(
            name="Esmerilhadeira Industrial 4 1/2",
            id_code="eqp-001",
            serial_number="SN-123456",
            status=Equipment.StatusOptions.ATIVO
        )

    def test_equipment_str_formatted_string(self):
        """Testa o método __str__ do modelo Equipment."""
        equipment = self.equipment
        expected_str = "EQP-001 - Esmerilhadeira Industrial 4 1/2 (Ativo / Operacional)"
        self.assertEqual(str(equipment), expected_str)

    def test_id_code_is_normalized_to_uppercase(self):
        """Testa se o id_code é normalizado para caixa alta e sem espaços."""
        equipment = self.equipment
        self.assertEqual(equipment.id_code, "EQP-001")


class EquipmentViewTest(TestCase):

    def setUp(self):
        """Prepara a URL e limpa/cria a base de dados inicial do teste."""
        self.url = reverse('equipamentos')
        
        # Cria 2 equipamentos ATIVOS
        self.eq1 = create_equipment(
            name="Elevador Hidráulico",
            id_code="EQP-001",
            serial_number="SN-111",
            status=Equipment.StatusOptions.ATIVO
        )
        self.eq2 = create_equipment(
            name="Compressor de Ar",
            id_code="EQP-002",
            serial_number="SN-222",
            status=Equipment.StatusOptions.ATIVO
        )

        # Cria 1 equipamento EM MANUTENÇÃO (para validar a contagem de ativos)
        self.eq3 = create_equipment(
            name="Scanner de Diagnóstico",
            id_code="EQP-003",
            serial_number="SN-333",
            status=Equipment.StatusOptions.MANUTENCAO
        )

    def test_equipments_name_is_rendered(self):
        """Testa se o nome do equipamento é renderizado corretamente."""
        response = self.client.get(self.url)
        self.assertContains(response, "Scanner de Diagnóstico")

    def test_equipments_views_status_code_200(self):
        """Testa se a view de listagem de equipamentos retorna status code 200."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_equipments_views_uses_correct_template(self):
        """Testa se a view de listagem de equipamentos utiliza o template correto."""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'equipamentos.html')

    def test_equipments_view_contains_all_equipments_in_context(self):
        """Teste de listagem: Valida se a QuerySet no contexto contem os itens criados."""
        response = self.client.get(self.url)

        # Recupera a chave 'equipments' passada no dicionario de contexto
        equipments_in_context = response.context['equipments']

        self.assertEqual(len(equipments_in_context), 3)
        self.assertIn(self.eq1, equipments_in_context)
        self.assertIn(self.eq2, equipments_in_context)
        self.assertIn(self.eq3, equipments_in_context)

    def test_equipments_view_calculates_total_ativos_correctly(self):
        """Teste total_ativos: Valida se o contador do contexto filtra apenas os ATIVOS."""
        response = self.client.get(self.url)

        # Apenas eq1 e eq2 possuem status ATIVO (eq3 está EM MANUTENÇÃO)
        self.assertEqual(response.context['total_ativos'], 2)
        self.assertEqual(response.context['total_equipamentos'], 3)

    def test_equipments_view_handles_empty_list(self):
        """Teste da lista vazia: Valida o comportamento quando o banco nao possui registros."""
        # Apaga todos os equipamentos criados pelo setUp
        Equipment.objects.all().delete()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['equipments']), 0)
        self.assertEqual(response.context['total_ativos'], 0)

        # Opcional: Garante que a mensagem amigavel de lista vazia foi renderizada no HTML
        self.assertContains(response, "Nenhum equipamento cadastrado")
