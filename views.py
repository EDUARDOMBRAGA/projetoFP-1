from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime
from django.db.models import Q
from caixas.models import Conta
from pessoas.models import Pessoa

def FluxoCaixaListar(request):
	fluxo = Conta
	return render(request, 'fluxos/FluxoCaixaListar.html',{'fluxo': fluxo})