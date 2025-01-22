from django.shortcuts import render, redirect
from .forms import ClimogramaForm
import matplotlib.pyplot as plt
import io
import base64
import numpy as np

def criar_climograma(request):
    if request.method == 'POST':
        form = ClimogramaForm(request.POST)
        if form.is_valid():
            climograma = form.save(commit=False)
            climograma.save()

            escala_precip = form.cleaned_data['escala_precipitacao']
            escala_temp = form.cleaned_data['escala_temperatura']
            precip_mensal = form.cleaned_data['precipitacao_mensal']
            temp_mensal = form.cleaned_data['temperatura_mensal']
            nome_local = form.cleaned_data['nome_local']
            nome_user = form.cleaned_data['nome_user']

            meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
                     'jul', 'ago', 'set', 'out', 'nov', 'dez']

            fig, ax1 = plt.subplots(figsize=(10, 6))
            
            ax1.bar(meses, precip_mensal, color='blue', label='Precipitação (mm)', alpha=0.6, linewidth=2)
            ax1.set_ylim(0, max(precip_mensal) + escala_precip)
            ax1.set_ylabel('Precipitação (mm)', color="blue")
            ax1.tick_params(axis='y', labelcolor='blue')
            precip_ticks = list(range(0, int(max(precip_mensal) + escala_precip), escala_precip))
            ax1.set_yticks(precip_ticks)

            ax2 = ax1.twinx()
            ax2.plot(meses, temp_mensal, color='green', marker='o', label='Temperatura (°C)')
            ax2.set_ylim(0, max(temp_mensal) + escala_temp)
            ax2.set_ylabel('Temperatura (°C)', color='green')
            ax2.tick_params(axis='y', labelcolor='green')
            temp_ticks = list(range(0, int(max(temp_mensal) + escala_temp), escala_temp))
            ax2.set_yticks(temp_ticks)

            fig.suptitle(f"Climograda de {nome_local}")
            fig.text(0.5, 0.02, f"AUTOCLIMA | Climograma feito por {nome_user}", ha='center', fontsize=10, color='black')
            ax1.grid(False, which='major', axis='x')
            ax2.grid(False, which='major', axis='x')
            ax1.grid(True, which='major', axis='y')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graphic = base64.b64encode(image_png).decode('utf-8')

            return render(request, 'climograma/sucesso.html', {'graphic': graphic})
        else:
            return render(request, 'climograma/form.html', {'form': form})
    else:
        form = ClimogramaForm()
        return render(request, 'climograma/form.html', {'form': form})

def sucesso(request):
    return render(request, 'climograma/sucesso.html')
