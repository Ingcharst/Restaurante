from django import forms
from .models import cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['identificacion', 'nombre', 'apellido', 'email', 'telefono', 'direccion']
        labels = {
            'identificacion': 'Identificación',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'pedidos': 'Pedidos realizados'
        }
        widgets = {
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'pedidos': forms.NumberInput(attrs={'class': 'form-control'})
        }