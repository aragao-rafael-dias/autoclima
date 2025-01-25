from django import forms
from .models import ClimogramaData

class ClimogramaForm(forms.ModelForm):

    OPCOES_PER = [
        ('1', 'Anual'),
        ('2', 'Mensal'),
        ('3', 'Semanal')
    ]

    periodo_escolha = forms.ChoiceField(
        choices=OPCOES_PER,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Selecione o período",
    )

    # ANUAL
    precip_ano_1 = forms.IntegerField(label="Janeiro", required= False)
    precip_ano_2 = forms.IntegerField(label="Fevereiro", required= False)
    precip_ano_3 = forms.IntegerField(label="Março", required=False)
    precip_ano_4 = forms.IntegerField(label="Abril", required=False)
    precip_ano_5 = forms.IntegerField(label="Maio", required=False)
    precip_ano_6 = forms.IntegerField(label="Junho", required=False)
    precip_ano_7 = forms.IntegerField(label="Julho", required=False)
    precip_ano_8 = forms.IntegerField(label="Agosto", required=False)
    precip_ano_9 = forms.IntegerField(label="Setembro", required=False)
    precip_ano_10 = forms.IntegerField(label="Outubro", required=False)
    precip_ano_11 = forms.IntegerField(label="Novembro", required=False)
    precip_ano_12 = forms.IntegerField(label="Dezembro", required=False)

    temp_ano_1 = forms.DecimalField(label="Janeiro", required=False, max_digits=5, decimal_places=2)
    temp_ano_2 = forms.DecimalField(label="Fevereiro", required=False, max_digits=5, decimal_places=2)
    temp_ano_3 = forms.DecimalField(label="Março", required=False, max_digits=5, decimal_places=2)
    temp_ano_4 = forms.DecimalField(label="Abril", required=False, max_digits=5, decimal_places=2)
    temp_ano_5 = forms.DecimalField(label="Maio", required=False, max_digits=5, decimal_places=2)
    temp_ano_6 = forms.DecimalField(label="Junho", required=False, max_digits=5, decimal_places=2)
    temp_ano_7 = forms.DecimalField(label="Julho", required=False, max_digits=5, decimal_places=2)
    temp_ano_8 = forms.DecimalField(label="Agosto", required=False, max_digits=5, decimal_places=2)
    temp_ano_9 = forms.DecimalField(label="Setembro", required=False, max_digits=5, decimal_places=2)
    temp_ano_10 = forms.DecimalField(label="Outubro", required=False, max_digits=5, decimal_places=2)
    temp_ano_11 = forms.DecimalField(label="Novembro", required=False, max_digits=5, decimal_places=2)
    temp_ano_12 = forms.DecimalField(label="Dezembro", required=False, max_digits=5, decimal_places=2)

    # MENSAL
    precip_mes_1 = forms.IntegerField(label="Semana 1", required=False)
    precip_mes_2 = forms.IntegerField(label="Semana 2", required=False)
    precip_mes_3 = forms.IntegerField(label="Semana 3", required=False)
    precip_mes_4 = forms.IntegerField(label="Semana 4", required=False)

    temp_mes_1 = forms.DecimalField(label="Semana 1", required=False, max_digits=5, decimal_places=2)
    temp_mes_2 = forms.DecimalField(label="Semana 2", required=False, max_digits=5, decimal_places=2)
    temp_mes_3 = forms.DecimalField(label="Semana 3", required=False, max_digits=5, decimal_places=2)
    temp_mes_4 = forms.DecimalField(label="Semana 4", required=False, max_digits=5, decimal_places=2)

    # SEMANAL
    precip_sem_dom = forms.IntegerField(label="Domingo", required=False)
    precip_sem_seg = forms.IntegerField(label="Segunda-feira", required=False)
    precip_sem_ter = forms.IntegerField(label="Terça-feira", required=False)
    precip_sem_qua = forms.IntegerField(label="Quarta-feira", required=False)
    precip_sem_qui = forms.IntegerField(label="Quinta-feira", required=False)
    precip_sem_sex = forms.IntegerField(label="Sexta-feira", required=False)
    precip_sem_sab = forms.IntegerField(label="Sábado", required=False)

    temp_sem_dom = forms.IntegerField(label="Domingo", required=False)
    temp_sem_seg = forms.IntegerField(label="Segunda-feira", required=False)
    temp_sem_ter = forms.IntegerField(label="Terça-feira", required=False)
    temp_sem_qua = forms.IntegerField(label="Quarta-feira", required=False)
    temp_sem_qui = forms.IntegerField(label="Quinta-feira", required=False)
    temp_sem_sex = forms.IntegerField(label="Sexta-feira", required=False)
    temp_sem_sab = forms.IntegerField(label="Sábado", required=False)

    class Meta:
        model = ClimogramaData
        fields = ['escala_precipitacao', 'escala_temperatura', 'nome_local', 'nome_user', 'periodo_escolha']

    def clean(self):
        cleaned_data = super().clean()
        
        # ANO 
        cleaned_data['precipitacao_anual'] = [
            cleaned_data['precip_ano_1'], cleaned_data['precip_ano_2'],
            cleaned_data['precip_ano_3'], cleaned_data['precip_ano_4'],
            cleaned_data['precip_ano_5'], cleaned_data['precip_ano_6'],
            cleaned_data['precip_ano_7'], cleaned_data['precip_ano_8'],
            cleaned_data['precip_ano_9'], cleaned_data['precip_ano_10'],
            cleaned_data['precip_ano_11'], cleaned_data['precip_ano_12'],
        ]
        cleaned_data['temperatura_anual'] = [
            cleaned_data['temp_ano_1'], cleaned_data['temp_ano_2'],
            cleaned_data['temp_ano_3'], cleaned_data['temp_ano_4'],
            cleaned_data['temp_ano_5'], cleaned_data['temp_ano_6'],
            cleaned_data['temp_ano_7'], cleaned_data['temp_ano_8'],
            cleaned_data['temp_ano_9'], cleaned_data['temp_ano_10'],
            cleaned_data['temp_ano_11'], cleaned_data['temp_ano_12'],
        ]

        # MÊS 
        cleaned_data['precipitacao_mensal'] = [
            cleaned_data['precip_mes_1'], cleaned_data['precip_mes_2'],
            cleaned_data['precip_mes_3'], cleaned_data['precip_mes_4'],
        ]

        cleaned_data['temperatura_mensal'] = [
            cleaned_data['temp_mes_1'], cleaned_data['temp_mes_2'],
            cleaned_data['temp_mes_3'], cleaned_data['temp_mes_4'],
        ]

        # SEMANA
        cleaned_data['precipitacao_semanal'] = [
            cleaned_data['precip_sem_dom'], cleaned_data['precip_sem_seg'],
            cleaned_data['precip_sem_ter'], cleaned_data['precip_sem_qua'],
            cleaned_data['precip_sem_qui'], cleaned_data['precip_sem_sex'],
            cleaned_data['precip_sem_sab'],
        ]

        cleaned_data['temperatura_semanal'] = [
            cleaned_data['temp_sem_dom'], cleaned_data['temp_sem_seg'],
            cleaned_data['temp_sem_ter'], cleaned_data['temp_sem_qua'],
            cleaned_data['temp_sem_qui'], cleaned_data['temp_sem_sex'],
            cleaned_data['temp_sem_sab'],
        ]


        return cleaned_data
