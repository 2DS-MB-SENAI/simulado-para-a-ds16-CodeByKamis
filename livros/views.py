from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def listar_livros(request):
    livraria = Livro.objects.all()
    return render(request, 'livros.html', {'livraria':livraria})

@api_view(['GET'])
def read_livros(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def creat_livros(request):
    if request.method == 'POST':
        serializer= LivroSerializer(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)