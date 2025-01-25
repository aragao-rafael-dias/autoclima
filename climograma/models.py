from django.db import models

class ClimogramaData(models.Model):
    class PeriodoEscolha(models.IntegerChoices):
        ANUAL = 1, 'Anual'
        MENSAL = 2, 'Mensal'
        SEMANAL = 3, 'Semanal'


    escala_precipitacao = models.IntegerField()
    escala_temperatura = models.IntegerField()
    
    precipitacao_anual = models.JSONField(blank=True, null=True)
    temperatura_anual = models.JSONField(blank=True, null=True)

    precipitacao_mensal = models.JSONField(blank=True, null=True)
    temperatura_mensal = models.JSONField(blank=True, null=True)

    precipitacao_semanal = models.JSONField(blank=True, null=True)
    temperatura_semanal = models.JSONField(blank=True, null=True)

    periodo_escolha = models.IntegerField(choices=PeriodoEscolha.choices, default=PeriodoEscolha.MENSAL)
    nome_local = models.CharField(max_length=100, default='Local desconhecido')
    nome_user = models.CharField(max_length=100, default='Seu Nome')

    def __str__(self):
        return f"Climograma: {self.nome_local} - Criado por {self.nome_user}"