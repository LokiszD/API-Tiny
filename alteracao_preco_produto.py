import requests

token = '08a9511b372a1df214ef0000a79a0ae22a464073'
urlPesqProd = 'https://api.tiny.com.br/api2/produtos.pesquisa.php'
paramsPesqProd = {
    'token': token,
    'formato': 'json',
    'pesquisa': '',
    'pagina': 1
}

paginaAtual = 1
cont = 0

try:

    while True:
        print(f'Página: {paginaAtual}')
        paramsPesqProd['pagina'] = paginaAtual
        response = requests.get(url=urlPesqProd, params=paramsPesqProd)
        pesqProdJson = response.json()
        produtos = pesqProdJson['retorno']['produtos']

        # looping para pegar todos produtos
        for produto in produtos:
            nomeProd = produto['produto']['nome']
            cod = produto['produto']['codigo']
            preco = produto['produto']['preco']
            precoPromo = produto['produto']['preco_promocional']
            precoCusto = produto['produto']['preco_custo']
            precoCustoMedio = produto['produto']['preco_custo_medio']
            tipoVariacao = produto['produto']['tipoVariacao'] # Tipo de variação "N" - Normal, "P" - Pai, "V" - Variação

            print(f'Nome: {nomeProd:75} Cod Produto: {cod:15} Preço: {preco:7} Preço Promocional: {precoPromo:5} Preço Custo: {precoCusto:5} Preço Custo Médio: {precoCustoMedio:5} Tipo Variação: {tipoVariacao}')
            cont += 1
        paginaAtual += 1

except:
    print(f'\nTotal de Produtos: {cont}\nFINALIZADO...')
