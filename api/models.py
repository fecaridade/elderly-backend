from django.db import models

# Create your models here.


class Atividade(models.Model):
    valid_days = (
        ("Segunda", "Segunda"),
        ("Terça", "Terça"),
        ("Quarta", "Quarta"),
        ("Quinta", "Quinta"),
        ("Sexta", "Sexta"),
        ("Sábado", "Sábado"),
        ("Domingo", "Domingo"),
    )
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    dia_semana = models.CharField(max_length=30)
    gif_exercicio = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome + " - " + self.dia_semana
