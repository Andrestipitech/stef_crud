from django.db import models

class Auto(models.Model):
    idpbv = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    cc = models.IntegerField()
    especificaciones = models.TextField()

    def __str__(self):
        return f'{self.marca}, {self.modelo}'