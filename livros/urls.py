from django.urls import path
from .import views

urlpatterns =[
    path('livros/',views.listar_livros, name='listar_livros'),
    path('livros/read/', views.read_livros, name='read_livros'),
    path('livros/criar/', views.creat_livros, name='creat_livros'),
]