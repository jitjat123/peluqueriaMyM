from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Direccion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ciudad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user) or ''


    class Meta:
        db_table='direccion'
        verbose_name='Direccion'
        verbose_name_plural='Direcciones'
        ordering=['id']