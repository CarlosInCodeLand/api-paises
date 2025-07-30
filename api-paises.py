import json
import requests
import sys

url_all = "https://restcountries.com/v3.1/independent?status=true"
url_capital = "https://restcountries.com/v3.1/capital/"
def requisicao(url):
    try:
       resposta = requests.get(url)
       if resposta.status_code == 200:
           return resposta.text
    except:
       print(f'Erro ao fazer requisicao em {url}')

def tratamento(texto):
    try:
        return json.loads(texto)
    except Exception as e:
        print(f'Erro ao fazer parsing: {e}')

def numeroPaises():
    resposta = requisicao(url_all)
    if resposta:
        lista_paises = tratamento(resposta)
        if lista_paises:
            return len(lista_paises)

def mostrarPaises():
    resposta = requisicao(url_all)
    lista = tratamento(resposta)
    if lista:
        paises = []
        for pais in lista:
            paises.append(pais["name"]["common"])
        paises.sort()
        for i in paises:
            print(i)

def mostrarCapital(nome_pais):
    resposta = requisicao(url_capital+nome_pais)
    listaDePaises = tratamento(resposta)
    if listaDePaises:
        for pais in listaDePaises:
            print(pais['name']['common'], pais['capital'][0])
    else:
        print('Pais nao encontrado')

def mostrarPopulacao(nome):
    resposta = requisicao(url_all)
    lista_de_paises = tratamento(resposta)
    population = {}
    if lista_de_paises:
        for pais in lista_de_paises:
            population[pais['name']['common']] = pais['population']
        if nome in population:
            print(nome, population[nome])
    else:
        print('Pais nao encontrado')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('#' * 50)
        print('Bem vindo a consulta de Paises')
        print('#' * 50)
        print('Modo de uso python3 api-paises.py <acao> <nome do pais>')
        print('Acoes disponiveis:\ncontagem\npaises\ncapitais\npopulacao')
        print('#' * 50)
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            print(f'Existem {numeroPaises()} paises independentes no mundo')
            exit(0)

        elif argumento1 == 'paises':
            mostrarPaises()

        elif argumento1 == 'capitais':
            if len(sys.argv) > 2:
                argumento2 = sys.argv[2]
                print(mostrarCapital(argumento2))
            else:
                print('E preciso passar o nome do pais')
        
        elif argumento1 == 'populacao':
            if len(sys.argv) > 2:
                argumento2 = sys.argv[2]
                mostrarPopulacao(argumento2)
            else:
                print('E preciso passar o nome do pais')