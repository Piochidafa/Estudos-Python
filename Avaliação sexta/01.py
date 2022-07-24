import random


def cria_matriz(num_linhas, num_colunas):

    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(random.Random.randint(1,10))
            linha.append(valor)

        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)

m = le_matriz()

cria_matriz(50,50)