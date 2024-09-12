from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('criar_pedido/', views.criar_pedido, name='criar_pedido'),
]