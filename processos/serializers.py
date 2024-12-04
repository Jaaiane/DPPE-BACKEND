# processos/serializers.py
from rest_framework import serializers

class ProcessoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    area = serializers.CharField()
    data_abertura = serializers.CharField()
    status = serializers.CharField()
    ultimas_atualizacoes = serializers.CharField()