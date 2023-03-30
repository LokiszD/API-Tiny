from pesquisa_expedicao import PesquisaExpedicao
from identificador_pedido_ecommerce import PedidoEcommerce
from estoque_produto import EstoqueProdutos

# Parametros da API
token = '72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762' # Cookie

while True:
    numeroMenu = str(input('Digite 1 para ir ao Menu de Expedição\nDigite 2 para ir ao Menu de Pedidos do Ecommerce\nDigite 3 para conferir os produtos com saldo negativo ou zerado\nDigito: '))
    if numeroMenu == '1' or numeroMenu == '2' or numeroMenu == '3':
        break
    else:
        print('Digito Invalido, tente novamente...\n')

if numeroMenu == '1':
    # Rodar Pesquisa de Expedição
    PesquisaExpedicao(token).rodarPesquisaExpedicao()

elif numeroMenu == '2':
    # Rodar pedidos do Ecommerce
    dataInicio = input('Data Inicial (dd/mm/aaaa): ')
    dataFinal = input('Data Final (dd/mm/aaaa): ')
    PedidoEcommerce(token, dataInicio, dataFinal).rodarPedidoEcommerce()

elif numeroMenu == '3':
    # Estoque zerado ou negativo - gera um txt
    EstoqueProdutos(token).rodarEstoqueNegativoZerado()


