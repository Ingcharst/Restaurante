from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_sesion, name='inicio_sesion'),
    path('Cliente/', views.Cliente, name='Cliente'),
    path('menu/', views.menu, name='menu'),
    path('pedido/<int:plato_id>/', views.hacerpedido, name='hacerpedido'),
    path('cocina/', views.pedidoscocina, name='pedidoscocina'),
    path('cambiarestado/<int:pedido_id>/', views.cambiarestado, name='cambiarestado'),
    path('pedidocliente/cliente_identificacion/', views.pedidocliente, name='pedidocliente'),
    path('cliente/<int:identificacion_id>/', views.cliente, name='cliente'),
]
