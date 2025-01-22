from django import forms
from .models import ClimogramaData

class ClimogramaForm(forms.ModelForm):
    precip_mes_1 = forms.IntegerField(label="Janeiro", required=True)
    precip_mes_2 = forms.IntegerField(label="Fevereiro", required=True)
    precip_mes_3 = forms.IntegerField(label="Março", required=True)
    precip_mes_4 = forms.IntegerField(label="Abril", required=True)
    precip_mes_5 = forms.IntegerField(label="Maio", required=True)
    precip_mes_6 = forms.IntegerField(label="Junho", required=True)
    precip_mes_7 = forms.IntegerField(label="Julho", required=True)
    precip_mes_8 = forms.IntegerField(label="Agosto", required=True)
    precip_mes_9 = forms.IntegerField(label="Setembro", required=True)
    precip_mes_10 = forms.IntegerField(label="Outubro", required=True)
    precip_mes_11 = forms.IntegerField(label="Novembro", required=True)
    precip_mes_12 = forms.IntegerField(label="Dezembro", required=True)

    temp_mes_1 = forms.DecimalField(label="Janeiro", required=True, max_digits=5, decimal_places=2)
    temp_mes_2 = forms.DecimalField(label="Fevereiro", required=True, max_digits=5, decimal_places=2)
    temp_mes_3 = forms.DecimalField(label="Março", required=True, max_digits=5, decimal_places=2)
    temp_mes_4 = forms.DecimalField(label="Abril", required=True, max_digits=5, decimal_places=2)
    temp_mes_5 = forms.DecimalField(label="Maio", required=True, max_digits=5, decimal_places=2)
    temp_mes_6 = forms.DecimalField(label="Junho", required=True, max_digits=5, decimal_places=2)
    temp_mes_7 = forms.DecimalField(label="Julho", required=True, max_digits=5, decimal_places=2)
    temp_mes_8 = forms.DecimalField(label="Agosto", required=True, max_digits=5, decimal_places=2)
    temp_mes_9 = forms.DecimalField(label="Setembro", required=True, max_digits=5, decimal_places=2)
    temp_mes_10 = forms.DecimalField(label="Outubro", required=True, max_digits=5, decimal_places=2)
    temp_mes_11 = forms.DecimalField(label="Novembro", required=True, max_digits=5, decimal_places=2)
    temp_mes_12 = forms.DecimalField(label="Dezembro", required=True, max_digits=5, decimal_places=2)

    class Meta:
        model = ClimogramaData
        fields = ['escala_precipitacao', 'escala_temperatura', 'nome_local', 'nome_user']

    def clean(self):
        cleaned_data = super().clean()
        
        cleaned_data['precipitacao_mensal'] = [
            cleaned_data['precip_mes_1'], cleaned_data['precip_mes_2'],
            cleaned_data['precip_mes_3'], cleaned_data['precip_mes_4'],
            cleaned_data['precip_mes_5'], cleaned_data['precip_mes_6'],
            cleaned_data['precip_mes_7'], cleaned_data['precip_mes_8'],
            cleaned_data['precip_mes_9'], cleaned_data['precip_mes_10'],
            cleaned_data['precip_mes_11'], cleaned_data['precip_mes_12'],
        ]
        cleaned_data['temperatura_mensal'] = [
            cleaned_data['temp_mes_1'], cleaned_data['temp_mes_2'],
            cleaned_data['temp_mes_3'], cleaned_data['temp_mes_4'],
            cleaned_data['temp_mes_5'], cleaned_data['temp_mes_6'],
            cleaned_data['temp_mes_7'], cleaned_data['temp_mes_8'],
            cleaned_data['temp_mes_9'], cleaned_data['temp_mes_10'],
            cleaned_data['temp_mes_11'], cleaned_data['temp_mes_12'],
        ]

        return cleaned_data
