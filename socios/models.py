from django.db import models

# Create your models herePara el sistema se necesitará almacenar, el nombre del socio, fecha incorporación, año de
#nacimiento, teléfono, correo electrónico, sexo, estado (Vigente, Suspendido, Retirado),
#observacion

class Socios(models.Model):
    nombre = models.CharField(max_length=90)
    fechaIncorporacion = models.DateField()
    añoNacimiento = models.DateField()
    telefono = models.CharField(max_length=13)
    correo = models.EmailField()
    sexo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    observacion = models.TextField(blank=True)











