from django.shortcuts import render
from .models import Receita
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.
def index(request):
    dados = {
        'receitas': Receita.objects.all()
    }

    return render(request, 'index.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_a_exibir)
