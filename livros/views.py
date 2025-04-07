from django.shortcuts import render
from .models import Livraria
def listar_livros(request):
    livraria = Livraria.objects.all().order_by('-data_criacao')
    return render(request, 'templates/livros.html', {'livraria':livraria})

# Create your views here.
