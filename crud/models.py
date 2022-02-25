from django.db import models

class Ropa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.ImageField(null=True,blank=True)
