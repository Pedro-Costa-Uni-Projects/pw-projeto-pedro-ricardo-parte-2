from django.db import models


# Create your models here.
class Contacto(models.Model):
    nome = models.CharField(max_length=40)
    apelido = models.CharField(max_length=40)
    email = models.EmailField()
    opcoesPais = [
        ("pt", "Portugal"),
        ("br", "Brasil"),
        ("esp", "Espanha"),
        ("uk", "Reino Unido"),
        ("ale", "Alemanha"),
        ("bel", "Bélgica"),
        ("eua", "Estados Unidos")
    ]
    pais = models.CharField(max_length=20, choices=opcoesPais, default="")
    dataCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome + " " + self.apelido


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)

    clareza = models.CharField(max_length=10, default=3)

    rigor = models.CharField(max_length=10, default=3)

    precisao = models.CharField(max_length=10, default=3)

    optimizacao = models.BooleanField(verbose_name="Boa optimização para telemóvel", default=False)

    tempoResposta = models.BooleanField(verbose_name="Tempo de resposta do Website", default=False)

    facilUsar = models.BooleanField(verbose_name="Fácil de Usar", default=False)

    facilLer = models.BooleanField(verbose_name="Fácil de Ler", default=False)

    feedBack = models.TextField(default="")

    def __str__(self):
        return str(self.id)
