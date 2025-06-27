from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length= 50)
    

class Professor(models.Model):
    nome = models.CharField(max_length= 50)
    turma =  models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__ (self):
        return f"{self.nome} - chave do professor: {self.turma}"