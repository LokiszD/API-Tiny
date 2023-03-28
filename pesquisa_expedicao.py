import requests
from datetime import datetime


class PesquisaExpedicao:
    def __init__(self, token):
        self.token = token

    def rodarPesquisaExpedicao(self):
        print(f'=' * 20)
        print(f'Romaneio de Embarque')
        print(f'=' * 20)
        print('')

        # Parametros da API
        # token = '72be570119ddd8ab7b94cd7d93e9cd2aaaf9a762' # Cookie
        token = self.token
        # Inputs para estabelecer os filtros de pesquisa

        dataInicial = input('Escreva a data inicial (dd/mm/aaaa): ')
        dataFinal = input('Escreva a data final (dd/mm/aaaa): ')
        verificaData = True

        while verificaData:
            try:
                # verifica se a entrada está no formato correto de data
                datetime.strptime(dataInicial, '%d/%m/%Y')
                datetime.strptime(dataFinal, '%d/%m/%Y')
                verificaData = False
            except:
                print("A entrada não está no formato correto de data, tente novamente\n")
                dataInicial = input('Escreva a data inicial (dd/mm/aaaa): ')
                dataFinal = input('Escreva a data final (dd/mm/aaaa): ')

        formaEnvio = ''
        while formaEnvio != 'T' and formaEnvio != 'C' and formaEnvio != 'M':
            formaEnvio = input('Escreva a forma de envio (T=Transportadora/ C=Correios/ M=MercadoEnvios): ').upper()
        situacao = ''
        while situacao != 'A' and situacao != 'C' and situacao != 'T':
            situacao = input(
                'Escreva a situação que quer ver da expedição (A= Aguardando | C= Concluido | T= Todos): ').upper()
        print('')

        # Parametros da API de pesquisa de expedição
        url = 'https://api.tiny.com.br/api2/expedicao.pesquisa.php'
        params = {
            "token": self.token,
            "formato": "json",
            "formaEnvio": formaEnvio,
            "pagina": 1,
            "dataInicial": dataInicial,
            "dataFinal": dataFinal
        }

        # Definir nomes das formas de envio
        if formaEnvio == 'T':
            formaEnvio = 'Transportadora'
        elif formaEnvio == 'C':
            formaEnvio = 'Correios'
        elif formaEnvio == 'M':
            formaEnvio = 'Mercado Envios'

        cont = 0
        print(f'-' * 175)
        # While para pegar todas as paginas da API

        paginaAtual = 1
        try:
            while True:
                params['pagina'] = paginaAtual
                response = requests.get(url=url, params=params)
                respostaJson = response.json()
                expedicoes = respostaJson['retorno']['expedicoes']

                for expedicao in expedicoes:  # looping para passar por todas expedições
                    expedicaoSituacao = expedicao['expedicao']['situacao']
                    qtdVolume = expedicao['expedicao']['qtdVolumes']
                    idNotaFiscal = expedicao['expedicao']['idObjeto']
                    destinatarioNnome = expedicao['expedicao']['destinatario']['nome']
                    dataEmissao = expedicao['expedicao']['dataEmissao']

                    if expedicaoSituacao == '0':
                        expedicaoSituacao = 'Aguardando'
                    else:
                        expedicaoSituacao = 'Concluido'

                    if situacao == 'A':  # Pegar apenas status com situação AGUARDANDO
                        if expedicaoSituacao == 'Aguardando':
                            print(
                                f'ID da Nota Fiscal: {idNotaFiscal:15} {formaEnvio}\n{destinatarioNnome} \nSituação: {expedicaoSituacao:15}\nQuantidade Vol: {qtdVolume:5} Data de Emissão: {dataEmissao:15}')
                            print(f'-' * 100)
                            cont += 1
                    elif situacao == 'C':  # Pegar apenas status com situação Concluido
                        if expedicaoSituacao == 'Concluido':
                            print(
                                f'ID da Nota Fiscal: {idNotaFiscal:15} {formaEnvio}\n{destinatarioNnome} \nSituação: {expedicaoSituacao:15}\nQuantidade Vol: {qtdVolume:5} Data de Emissão: {dataEmissao:15}')
                            print(f'-' * 100)
                            cont += 1
                    else:  # Pegar todos status
                        print(
                            f'ID da Nota Fiscal: {idNotaFiscal:15} {formaEnvio}\n{destinatarioNnome} \nSituação: {expedicaoSituacao:15}\nQuantidade Vol: {qtdVolume:5} Data de Emissão: {dataEmissao:15}')
                        print(f'-' * 100)
                        cont += 1
                paginaAtual += 1
        except:
            print(f'Terminou, {cont} Resultados')

        print('Assinatura do Motorista: ')
        print('Assinatura do Operador de Embarque: ')
