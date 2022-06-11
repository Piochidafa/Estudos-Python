'''
p = [[],[]]

for i in range(0, 1):
    for j in range(0, 2):
        p[i][j] = int(input("qual seu nome: "))

print(p)

'''

#  print("nome",nome_pessoa,"idade",idade_pessoa,"id",id_pessoa)

def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar Produtos
    2. Listar produtos
    3. Buscar produtos
    ''')

def cadastrar(produtos):
    produtos = []
    identificador = input('Id ')
    nome = input('Nome do produto ')
    quantidade = int(input('Quantidade'))
    produtos.append((identificador, nome, quantidade))

def listar(produtos):
    for produto in produtos:
        identificador, nome, quantidade = produto
        print(f'Nome do produto: {nome}, identificador: {identificador}, quantidade: {quantidade}')


def buscar(produtos):
    identificador_desejado = input('Id ')
    for produto in produtos:
        identificador, nome, quantidade = produto
        if identificador == identificador_desejado:
            print(f'Nome do produto: {nome}, quantidade: {quantidade}, id: {identificador}')
            break
    else:
        print(f' Produto com id {identificador_desejado} não encontrado(a)')

def main():
    produtos = []

    while True:
        exibir_menu()
        opcao = int(input('Opção '))
        if opcao == 1:
            cadastrar(produtos)
        elif opcao == 2:
            listar(produtos)
        elif opcao == 3:
            buscar(produtos)
        else:
            print('Opção inválida')

main()

