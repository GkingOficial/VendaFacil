# Resumo
O sistema web em desenvolvimento é voltado para a gestão de vendas destinado a pequenas e médias empresas. Seu principal objetivo é otimizar o gerenciamento de produtos, controlar o estoque, acompanhar o fluxo de caixa e o histórico de compras, além de emitir alertas para produtos com baixo estoque.

O sistema busca resolver os desafios enfrentados por empresas menores que, muitas vezes, dependem de processos manuais ou sistemas limitados para gerenciar vendas e estoque. Ao automatizar essas tarefas, o software simplifica a operação, melhora a organização e ajuda os empresários a tomarem decisões mais informadas com base em relatórios precisos.

## Modelos
- Produto
- Pedido
- Fatura
- Usuário
- Histórico de compras
- Estoque
- Caixa

## Funcionalidades
- Cadastro completo de usuário, com gerenciamento, recuperação de senha, etc.
- Histórico de compras salvo no banco de dados para controle e fechamento de caixa.
- Acompanhamento das vendas do dia.
- Aviso automático de estoque baixo.
- Emissão de pedidos e faturas.
- Geração de relatórios de vendas.

# Aplicações

## Vendas
Responsável por gerenciar toda a lógica de vendas. Nele, o atendente pode adicionar produtos à venda, calcular o valor total, escolher a forma de pagamento, finalizar a venda e emitir o comprovante.

### Modelos
- Produto
- Pedido
- Fatura

### Funcionalidades
- Seleção de produtos por categoria ou código.
- Cálculo de valores individuais, totais e troco.
- Emissão de fatura ou comprovante de venda.
- Lógica para pagamento múltiplo (dinheiro, crédito, PIX, etc.).

## Estoque
Responsável por gerenciar o controle de estoque dos produtos disponíveis para venda. Ele rastreia a quantidade de cada item em estoque e emite alertas quando um produto atinge um nível baixo.

### Modelos
- Produto (referenciado aqui para gerenciar o estoque).

### Funcionalidades
- Controle de entradas e saídas de produtos.
- Emissão de alertas automáticos de estoque baixo.
- Relatórios de movimentação de estoque.

## Caixa
Esta aplicação lida com o controle financeiro, permitindo que o atendente veja o saldo diário e registre transações. Ele também gera relatórios financeiros e controla o fechamento de caixa.

### Modelos
- Transacao (para registrar entradas e saídas do caixa).
### Funcionalidades
- Controle do saldo inicial, vendas e outras transações financeiras.
- Fechamento de caixa diário.
- Relatórios financeiros e de fluxo de caixa.

## Delivery
Responsável por gerenciar as vendas de delivery. O atendente pode registrar pedidos de entrega, calcular o frete (usando uma API externa, como o Google Maps), e registrar as entregas realizadas.

### Modelos
- PedidoDelivery (um modelo específico para os pedidos via delivery).

### Funcionalidades
- Integração com API do Google Maps para cálculo de frete.
- Integração com WhatsApp para chamar motoboy de um grupo específico.

