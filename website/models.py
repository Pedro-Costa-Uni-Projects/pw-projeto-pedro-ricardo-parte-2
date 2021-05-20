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
