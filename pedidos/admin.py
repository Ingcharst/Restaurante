from django.contrib import admin
from .models import Plato, Pedido, cliente, acompanamiento

# Register your models here.

admin.site.register(Plato)
admin.site.register(Pedido)
admin.site.register(cliente)
admin.site.register(acompanamiento)



