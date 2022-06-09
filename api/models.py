from django.db import models

class Bibita(models.Model):
    codice = models.CharField(max_length=10)
    bevanda = models.CharField(max_length=30)
    prezzo = models.FloatField()

    def __str__(self):
        return self.bevanda


class Tessera(models.Model):
    codice = models.CharField(max_length=5)
    credito = models.FloatField()

    def __str__(self):
        return self.codice

class Colonna(models.Model):
    numeroCol = models.IntegerField()
    bibita = models.CharField(max_length=30)
    numeroLatt= models.IntegerField()

