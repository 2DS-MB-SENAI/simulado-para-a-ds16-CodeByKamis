from django.shortcuts import render
from .models import Livro
def listar_livros(request):
    livraria = Livro.objects.all()
    return render(request, 'livros.html', {'livraria':livraria})

# Create your views here.
