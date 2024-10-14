from django.shortcuts import render, redirect, get_object_or_404
from .models import Plato, Pedido, acompanamiento, cliente
from django.contrib.auth.decorators import login_required
from .forms import  ClienteForm
from django.contrib.auth import authenticate, login


# Create your views here.


@login_required
def menu(request):
    platos = Plato.objects.all()
    return render(request, 'menu.html', {'platos': platos})


@login_required
def hacerpedido(request, plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    acomp = plato.acompanamientos.all()
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
        total = cantidad * plato.precio
        pedido = Pedido(usuario=request.user, plato=plato, cantidad=cantidad, total=total)
        pedido.save()       
        return redirect('pedidoscocina')
    return render(request, 'hacerpedido.html', {'plato': plato,'acomp': acomp})


@login_required
def pedidoscocina(request):
    pedidos = Pedido.objects.filter(estado='Pendiente').order_by('fecha')
    return render(request, 'pedidoscocina.html', {'pedidos': pedidos})


@login_required
def cambiarestado(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        nuevo_estado = request.POST['estado']
        pedido.estado = nuevo_estado
        pedido.save()
        return redirect('pedidoscocina')
    return render(request, 'cambiarestado.html', {'pedido': pedido})


def pedidocliente(request):
    if request.method == 'POST':
        ident = request.POST.get('identificacion')
        clientes = cliente.objects.filter(identificacion=ident).first()
        if clientes:
            return render(request, 'hacerpedido.html', {'clientes': clientes})
        else:
            return render(request, 'registrocliente.html', {'no_encontrado': True})
    
    return render(request, 'registrocliente.html')

# def detalleplato(request, plato_id):
#     plato = get_object_or_404(Plato, id=plato_id)
#     acompanamientos = plato.acompanamientos.all() 

#     if request.method == 'POST':
#         acompanamientos = request.POST.getlist('acompanamientos')
#         seleccionados = acompanamiento.objects.filter(id__in=acompanamientos)
#         total = plato.precio(seleccionados)

#         return render(request, 'confirmar_pedido.html', {
#             'plato': plato,
#             'seleccionados': seleccionados,
#             'total': total,
#         })

#     return render(request, 'detalle_plato.html', {
#         'plato': plato,
#         'acompanamientos': acompanamientos,
#     })

# def cliente(request):
#     if request.method == 'POST':
#         nombre = request.POST['nombre']
#         apellido = request.POST['apellido']
#         identificacion = request.POST['identificacion']
#         direccion = request.POST['direccion']
#         telefono = request.POST['telefono']
#         email = request.POST['email']
#         Cliente = cliente(nombre=nombre, apellido=apellido, identificacion=identificacion, direccion=direccion, telefono=telefono, email=email)
#         Cliente.save()
#         return redirect('pedidoscocina')
#     return render(request, 'cliente.html')

def Cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicio_sesion')
    return render(request, 'cliente.html', {'form': form})
    


def inicio_sesion(request):
    if request.method == 'POST':
        identificacion = request.POST.get('identificacion')

        # Verifica si la identificación existe en la base de datos
        cliente_obj = cliente.objects.filter(identificacion=identificacion).first()
        
        if cliente_obj:
            request.session['cliente_id'] = cliente_obj.id  
            return redirect('menu')  
        else:
            return render(request, 'inicio_sesion.html', {'error': 'La identificación no se encuentra registrada!'})

    return render(request, 'inicio_sesion.html')


def actualizar(request, id):
        
    empleado = get_object_or_404(cliente, id=id)

    if request.method == "POST":

        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.identificacion = request.POST.get('identificacion')
        empleado.nombre = request.POST.get('email')
        empleado.nombre = request.POST.get('direccion')
        empleado.telefono = request.POST.get('telefono')
              
        empleado.save()
        
        return redirect('inicio_sesion')  
    return render(request, 'pedidos/actualizar.html', {'cliente_obj': empleado})


    
