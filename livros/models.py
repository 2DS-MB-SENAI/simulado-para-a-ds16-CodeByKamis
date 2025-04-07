from django.db import models

class Livraria(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    paginas = models.IntegerField()

    def __str__(self):
        return self.titulo

# Create your models here.

