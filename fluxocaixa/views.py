from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from caixas.models import Conta
from pessoas.models import Pessoa


def fluxoCaixa(request):
    if request.method == 'POST':
        pessoa = request.POST.get('buscaPessoa', '').upper()
        dataInicial = datetime.strptime(request.POST.get('dataInicial', ''), '%d/%m/%Y %H:%M:%S')
        dataFinal = datetime.strptime(request.POST.get('dataFinal', ''), '%d/%m/%Y %H:%M:%S')
        totalreceber = 0
        totalpagar = 0
        
        nome = Pessoa.objects.filter(id=buscaPessoa)
        pessoas = Pessoa.objects.all().order_by('nome')
        try:
            sql = ("select cc.* from caixas_conta cc inner join pessoas_pessoa pp on pp.id = cc.pessoa_id where pp.nome like '%s' order by data") % ('%%'+pessoa+'%%')
            contas = Conta.objects.raw(sql)

            for conta in contas:
                if conta.tipo == 'E':
                    totalreceber += conta.valor
                elif conta.tipo == 'S':
                    totalpagar -= conta.valor
            
        except:
            contas = []
        return render(request, 'fluxocaixa/fluxoCaixa.html', {'contas': contas, 'totalreceber': totalreceber, 'totalpagar': totalpagar})
    else:
        return render(request, 'fluxocaixa/fluxoCaixa.html')






    




