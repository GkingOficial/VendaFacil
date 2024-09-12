from django.contrib import admin
from .models import Produto, Pedido, Fatura

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Fatura)