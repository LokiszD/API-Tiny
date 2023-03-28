import requests
import csv

url = "https://api.tiny.com.br/api2/produtos.pesquisa.php"
params = {
    "token": "08a9511b372a1df214ef0000a79a0ae22a464073",
    "formato": "json",
    "campos": "idproduto",
    "pagina": 1
}

rows = []
try:
    while True:
        response = requests.get(url, params=params)
        respostaJson = response.json()
        produtos = respostaJson['retorno']['produtos']

        for produto in produtos:
            idProduto = produto['produto']['id']
            nomeProduto = produto['produto']['nome']
            # pegar estoque de todos os ids dos produtos
            urlEstoque = "https://api.tiny.com.br/api2/produto.obter.estoque.php?token=72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762&formato=json"
            paramsEstoque = {
                "token": "72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762",
                "formato": "json",
                "id": idProduto
            }
            response = requests.get(urlEstoque, params=paramsEstoque)
            estoqueJson = response.json()
            estoque = estoqueJson['retorno']['produto']['saldo']

            if estoque <= 0:
                rows.append([idProduto, nomeProduto, estoque])

        params["pagina"] += 1
except:
    print("Terminou")

with open('produtos_com_saldo_zero.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['ID', 'Nome', 'Saldo'])
    for row in rows:
        writer.writerow(row)