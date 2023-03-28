from pesquisa_expedicao import PesquisaExpedicao
from identificador_pedido_ecommerce import PedidoEcommerce
from estoque_produto import EstoqueProdutos

# Parametros da API
token = '72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762' # Cookie

# Rodar Pesquisa de Expedição
# PesquisaExpedicao(token).rodarPesquisaExpedicao()

# Rodar pedidos do Ecommerce
# dataInicio = '20/03/2023'
# dataFinal = '22/03/2023'
#
# PedidoEcommerce(token, dataInicio, dataFinal).rodarPedidoEcommerce()

# Estoque zerado ou negativo
EstoqueProdutos(token).rodarEstoqueNegativoZerado()

