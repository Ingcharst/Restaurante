from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class cliente(models.Model):
     identificacion = models.CharField(max_length=20)
     nombre = models.CharField(max_length=100)
     apellido = models.CharField(max_length=100)
     email = models.EmailField(null=True, blank=True)
     telefono = models.CharField(max_length=15, null=True, blank=True)
     direccion = models.CharField(max_length=255, null=True, blank=True)
     pedidos = models.PositiveIntegerField(default=0)

     def __str__(self):
         return self.nombre + " " + self.apellido


    
class acompanamiento(models.Model):
    ##Plato=models.ForeignKey(Plato, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre #+ " " + self.Plato.nombre



class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='platos/')
    acompanamientos = models.ManyToManyField(acompanamiento, related_name='platos')

    def __str__(self):
        return self.nombre
    
    def total(self, seleccion):
        valor = sum([a.precio for a in seleccion])
        return self.precio + valor



class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Preparando', 'Preparando'),
        ('Listo', 'Listo')
    ]
    clientes = models.ForeignKey(cliente, default="1", on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f'Pedido {self.id} - {self.usuario.username}' - {self.clientes.nombre} - {self.clientes.apellido}

