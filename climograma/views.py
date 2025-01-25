from django.shortcuts import render, redirect
from .forms import ClimogramaForm
import matplotlib.pyplot as plt
import io
import base64
import numpy as np
from django.http import JsonResponse
from django.template.loader import render_to_string

def carregar_template(request):
    periodo = request.GET.get('periodo')

    if periodo not in ['1', '2', '3']:
        return JsonResponse({'error': 'Opção de período inválida!'}, status=400)

    templates = {
        '1': 'climograma/anual.html',
        '2': 'climograma/mensal.html',
        '3': 'climograma/semanal.html',
    }
    template_name = templates.get(periodo)

    form = ClimogramaForm()

    html_content = render_to_string(template_name, {'form': form})
    return JsonResponse({'html': html_content})

def criar_climograma(request):
    if request.method == 'POST':
        form = ClimogramaForm(request.POST)
        if form.is_valid():
            escala_precip = max(1, form.cleaned_data['escala_precipitacao'])
            escala_temp = max(1, form.cleaned_data['escala_temperatura'])
            periodo_escolha = form.cleaned_data['periodo_escolha']

            precip_anual = form.cleaned_data.get('precipitacao_anual', [])
            temp_anual = form.cleaned_data.get('temperatura_anual', [])

            precip_mensal = form.cleaned_data.get('precipitacao_mensal', [])
            temp_mensal = form.cleaned_data.get('temperatura_mensal', [])

            precip_semanal = form.cleaned_data.get('precipitacao_semanal', [])
            temp_semanal = form.cleaned_data.get('temperatura_semanal', [])

            ano = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            mes = ['sem1', 'sem2', 'sem3', 'sem4']
            sem = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']

            if periodo_escolha == "1":
                periodo, precip, temp = ano, precip_anual, temp_anual
            elif periodo_escolha == "2":
                periodo, precip, temp = mes, precip_mensal, temp_mensal
            elif periodo_escolha == "3":
                periodo, precip, temp = sem, precip_semanal, temp_semanal
            else:
                return render(request, 'climograma/form.html', {'form': form, 'error': 'Período inválido!'})

            try:
                precip = [float(p) for p in precip]
                temp = [float(t) for t in temp]
                assert len(periodo) == len(precip) == len(temp), "Dados inconsistentes!"
            except Exception as e:
                return render(request, 'climograma/form.html', {'form': form, 'error': f"Erro nos dados: {e}"})

            fig, ax1 = plt.subplots(figsize=(10, 6))
            
            max_precip = max(precip)
            max_temp = max(temp)
            
            width = 1
            bars = ax1.bar(periodo, precip, color='blue', alpha=0.6, label='Precipitação (mm)', width=width, edgecolor='darkblue', linewidth=1.5)
            ax1.set_ylim(0, max_precip + escala_precip if max_precip + escala_precip > max_precip else escala_precip)
            ax1.set_ylabel('Precipitação (mm)', color="blue")
            ax1.tick_params(axis='y', labelcolor='blue')

            ax2 = ax1.twinx()
            ax2.plot(periodo, temp, color='green', marker='o', label='Temperatura (°C)')
            ax2.set_ylim(0, max_temp + escala_temp if max_temp + escala_temp > max_temp else escala_temp)
            ax2.set_ylabel('Temperatura (°C)', color='green')
            ax2.tick_params(axis='y', labelcolor='green')

            ax1.set_xticks(periodo)
            ax1.set_xticklabels(periodo, rotation=45, ha='right')
            ax1.grid(True, which='both', axis='y', color='black', linestyle = '-', linewidth = 0.9)

            for bar in bars:
                height = bar.get_height()  
                ax1.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{height:.1f}', ha='center', va='center', color='black', fontsize=10)

            fig.suptitle(f"Climograma - {form.cleaned_data['nome_local']}")
            fig.text(0.5, .9, f'AUTOCLIMA | Climograma gerado por {form.cleaned_data['nome_user']}', ha='center', fontsize=12, color='black')

            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            graphic = base64.b64encode(buffer.getvalue()).decode('utf-8')
            buffer.close()

            return render(request, 'climograma/sucesso.html', {'graphic': graphic})
        else:
            return render(request, 'climograma/form.html', {'form': form})
    else:
        form = ClimogramaForm()
        return render(request, 'climograma/form.html', {'form': form})



def sucesso(request):
    return render(request, 'climograma/sucesso.html')
