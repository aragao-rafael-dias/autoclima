from django.db import models

class ClimogramaData(models.Model):
    escala_precipitacao = models.IntegerField()
    escala_temperatura = models.IntegerField()
    precipitacao_mensal = models.JSONField(blank=True, null=True)
    temperatura_mensal = models.JSONField(blank=True, null=True)
    nome_local = models.CharField(max_length=100, default='Local desconhecido')
    nome_user = models.CharField(max_length=100, default='Seu Nome')

    def __str__(self):
        return f"Climograma: Escala de {self.nome_local}mm"