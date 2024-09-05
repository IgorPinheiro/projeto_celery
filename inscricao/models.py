from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nome
    
    

