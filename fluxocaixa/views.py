from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa

def fluxoListar(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    return render(request, 'fluxocaixa/fluxoCaixa.html', {'pessoas': pessoas})

def fluxoCaixa(request):
    if request.method == 'POST':

        dataInicial = request.POST.get('dataInicial', '%d/%m/%Y')
        dataFinal = request.POST.get('dataFinal', '%d/%m/%Y')
        total = 0

        try:
            contas = Conta.objects.filter(data__range=(dataInicial, dataFinal))
            for conta in contas:
                total += conta.valor
        except:
            contas = []

        return render(request, 'fluxocaixa/fluxoCaixa.html', {'contas': contas, 'total': total, 'dataInicial': dataInicial, 'dataFinal': dataFinal})
    
    return render(request, 'fluxocaixa/fluxoCaixa.html', {'contas': []})
