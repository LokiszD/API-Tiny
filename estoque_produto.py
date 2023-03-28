import requests


class EstoqueProdutos:

    def __init__(self, token):
        self.token = token

    def rodarEstoqueNegativoZerado(self):
        url = "https://api.tiny.com.br/api2/produtos.pesquisa.php"

        token = self.token
        params = {
            "token": token,
            "formato": "json",
            "campos": "idproduto,nome",
            "pagina": 1
        }
        # token = '08a9511b372a1df214ef0000a79a0ae22a464073' #adecil

        cont = 0
        paginaAtual = 1

        try:
            while True:
                params['pagina'] = paginaAtual  # atualiza a página atual
                response = requests.get(url, params=params)
                respostaJson = response.json()
                produtos = respostaJson['retorno']['produtos']

                filename = "produtos_com_estoque_negativo.txt"
                with open(filename, "w") as f:
                    for produto in produtos:
                        idProduto = produto['produto']['id']
                        nomeProduto = produto['produto']['nome']
                        # pegar estoque de todos os ids dos produtos
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
                            line = f"Id: {idProduto}, Nome: {nomeProduto}, Saldo: {estoque}\n"
                            f.write(line)
                            cont += 1

                paginaAtual += 1
        except:
            print(f"Terminou\nTotal de produtos com estoque negativo ou igual a zero: {cont}")

        print(f"Arquivo {filename} salvo com sucesso")
