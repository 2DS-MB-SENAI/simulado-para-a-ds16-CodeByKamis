from django.urls import path
from .import views

urlpatterns =[
    path('livros/',views.listar_livros, name='listar_livros'),
]