from django.urls import path
from . import views

urlpatterns =[
    path('auth/registro/', view=views.registro, name='registro'),
    path('auth/login/', view=views.logar_usuario, name='logar_usuario')
]