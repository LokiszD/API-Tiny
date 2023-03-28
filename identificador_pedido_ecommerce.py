import requests


class PedidoEcommerce:
    def __init__(self, token, dataInicial, dataFinal):
        self.token = token
        self.dataInicial = dataInicial
        self.dataFinal = dataFinal

    def rodarPedidoEcommerce(self):
        print(f'=' * 40)
        print(f'Identificador de Pedidos no E-commerce')
        print(f'=' * 40)
        print('')

        urlPedido = 'https://api.tiny.com.br/api2/pedidos.pesquisa.php'
        urlNf = 'https://api.tiny.com.br/api2/notas.fiscais.pesquisa.php'
        # token = '08a9511b372a1df214ef0000a79a0ae22a464073'  # Adecil
        token = self.token
        dataInicial = self.dataInicial
        dataFinal = self.dataFinal

        cont = 0

        paramsProd = {
            "token": token,
            "formato": "json",
            "pagina": 1,
            "dataInicial": dataInicial,
            "dataFinal": dataFinal
        }
        paginaAtual = 1

        try:
            while True:
                # Pesquisa pedido
                paramsProd['pagina'] = paginaAtual  # atualiza a página atual
                responsePedido = requests.get(url=urlPedido, params=paramsProd)
                respostaJsonPedido = responsePedido.json()
                pedidos = respostaJsonPedido['retorno']['pedidos']

                print(f'Pagina Atual: {paginaAtual}')

                # passar por todos produtos
                for pedido in pedidos:
                    idPedido = pedido['pedido']['id']
                    numEcom = pedido['pedido']['numero_ecommerce']
                    situcaoPedido = pedido['pedido']['situacao']
                    valorPedido = pedido['pedido']['valor']

                    print(
                        f'ID do Pedido: {idPedido}Numero Ecommerce: {numEcom} Situação do Pedido: {situcaoPedido} Valor do Pedido: {valorPedido}')
                    # Pesquisa NF relacionado com numero_ecommerce
                    try:
                        paramsNf = {"token": token, "formato": "json", "numeroEcommerce": numEcom}
                        responseNF = requests.get(url=urlNf, params=paramsNf)
                        respostaNfJson = responseNF.json()
                        notas_fiscais = respostaNfJson['retorno']['notas_fiscais']

                        # looping para pegar todas notas do pedido
                        for nota_fiscal in notas_fiscais:
                            idNf = nota_fiscal['nota_fiscal']['id']
                            situacaoNf = nota_fiscal['nota_fiscal']['descricao_situacao']
                            nomeTransportadora = nota_fiscal['nota_fiscal']['transportador']['nome']
                            print(f'ID da NF: {idNf} Situação NF: {situacaoNf} Transportadora: {nomeTransportadora}')
                    except:
                        print('Sem NF')

                    print('-' * 75)
                    cont += 1

                paginaAtual += 1  # atualiza para a próxima página

        except:
            print(f'Terminou, {cont} Resultados')
