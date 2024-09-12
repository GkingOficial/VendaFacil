from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        self.nome

class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pedido {self.id} - {self.data}'
    
class Fatura(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)

    def __str__(self):
        return f'Fatura {self.id} - Pedido {self.pedido.id}'