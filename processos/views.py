# processos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from agendamento.models import Agendamento  # Ajuste o caminho de importação conforme necessário

class ProcessoList(APIView):
    def get(self, request):
        nome_usuario = request.query_params.get('nome_usuario')
        if not nome_usuario:
            return Response({"error": "Nome do usuário é necessário."}, status=status.HTTP_400_BAD_REQUEST)

        # Filtrar agendamentos pelo nome do usuário
        agendamentos = Agendamento.objects.filter(usuario__username=nome_usuario)

        if not agendamentos.exists():
            return Response({"message": "Nenhum agendamento encontrado para esse usuário."}, status=status.HTTP_404_NOT_FOUND)

        processos = []
        for agendamento in agendamentos:
            # Certifique-se de que data_hora está definido
            if agendamento.data_hora:
                data_abertura = agendamento.data_hora.date()
                hora_agendamento = agendamento.data_hora.time().strftime("%H:%M")  # Formata a hora
            else:
                data_abertura = "Processo ainda não foi aberto"
                hora_agendamento = "Hora ainda não foi definida"

            processo = {
                "id": agendamento.id,
                "area": agendamento.area.nome,
                "data_abertura": data_abertura,
                "hora_agendamento": hora_agendamento,  # Hora do agendamento
                "status": agendamento.status,
                "ultimas_atualizacoes": "Última atualização em: {}".format(agendamento.data_hora),
            }
            processos.append(processo)

        return Response(processos)  # Retorna diretamente a lista de processos
