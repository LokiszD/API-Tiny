import requests

url = "https://api.tiny.com.br/api2/produtos.pesquisa.php"
params = {
    "token": "72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762",
    "formato": "json",
    "campos": "idproduto,nome",
    "pagina": 1
}
token = '08a9511b372a1df214ef0000a79a0ae22a464073' #adecil


cont = 0
try:
    while True:
        response = requests.get(url, params=params)
        respostaJson = response.json()
        produtos = respostaJson['retorno']['produtos']


        for produto in produtos:
            idProduto = produto['produto']['id']
            nomeProduto = produto['produto']['nome']
            #pegar estoque de todos os ids dos produtos
            urlEstoque = "https://api.tiny.com.br/api2/produto.obter.estoque.php?token=08a9511b372a1df214ef0000a79a0ae22a464073&formato=json"
            paramsEstoque = {
                "token": token,
                "formato": "json",
                "id": idProduto
            }
            response = requests.get(urlEstoque, params=paramsEstoque)
            estoqueJson = response.json()
            estoque = estoqueJson['retorno']['produto']['saldo']

            if estoque <= 0:
                print(f'Id: {idProduto}, Nome: {nomeProduto}, Saldo: {estoque}')
                cont += 1

        params["pagina"] += 1
except:
  print("Terminou")


print(f"Total de produtos com estoque negativo ou igual a zero: {cont}")

from pathlib import Path

filename = "produtos_com_estoque_negativo.txt"
with open(filename, "w") as f:
    for produto in produtos:
        idProduto = produto['produto']['id']
        nomeProduto = produto['produto']['nome']
        #pegar estoque de todos os ids dos produtos
        urlEstoque = "https://api.tiny.com.br/api2/produto.obter.estoque.php?token=08a9511b372a1df214ef0000a79a0ae22a464073&formato=json"
        paramsEstoque = {
            "token": "72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762",
            "formato": "json",
            "id": idProduto
        }
        response = requests.get(urlEstoque, params=paramsEstoque)
        estoqueJson = response.json()
        estoque = estoqueJson['retorno']['produto']['saldo']

        if estoque <= 0:
            line = f"Id: {idProduto}, Nome: {nomeProduto}, Saldo: {estoque}\n"
            f.write(line)

print(f"Arquivo {filename} salvo com sucesso")