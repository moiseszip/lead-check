import csv
import re

#ler numeros
def ler_numeros_celulares(caminho_arquivo):
    numeros = []
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            numeros.append(linha[0])  # Assumindo que os números estão na primeira coluna
    return numeros

#remove os repetidos
def remover_numeros_repetidos(numeros):
    numeros_unicos = list(set(numeros))
    return numeros_unicos

#valida 1 numero
def validar_numero_celular(numero):
    padrao = r'^\+?55\s?[1-9]{2}\s?9[1-9][0-9]{3,4}[-\s]?[0-9]{4}$'
    return re.match(padrao, numero) is not None

#analisa todos
def analisar_numeros_celulares(numeros):
    numeros_validos = []
    numeros_invalidos = []

    for numero in numeros:
        if validar_numero_celular(numero):
            numeros_validos.append(numero)
        else:
            numeros_invalidos.append(numero)

    return numeros_validos, numeros_invalidos

#salva em uma nova lista
def salvar_numeros_arquivo(numeros, caminho_arquivo):
    with open(caminho_arquivo, 'w', newline='') as arquivo:
        for numero in numeros:
            for num in numero:
                arquivo.write(num + '\n')

lista_numeros = ler_numeros_celulares('lista_numeros.csv')
numeros_sem_repeticao = remover_numeros_repetidos(lista_numeros)
numeros_validos = analisar_numeros_celulares(numeros_sem_repeticao)
salvar_numeros_arquivo(numeros_validos, 'lista_numeros_ok.csv')