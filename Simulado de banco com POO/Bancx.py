
class ClienteDoBanco:

    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def apresentacao(self):
        print(f"\nOlá {self.nome} Eu sou o Cauã ^_____^,\ne estou utilizando esse mini banco como forma de estudo de POO")
        return

    def efetuarCompra(self):

        a = input(f"\n(1) - Arroz R$17,50\n(2) - Feijão R$9,90\n: ")

        if a == "1":
            print(f"\nCompra de Arroz efetuada\n")
            self.saldo = self.saldo - 17.50
            return

        elif a == "2":
            print(f"\nCompra de Feijão efetuada\n")
            self.saldo = self.saldo - 9.90
            return

        else:
            return print("\nValor Invalido")

    def emprestimo(self):
        a = input(F"\n______Olá SR.{self.nome} estamos com um emprestimo de________\n_"
              F"___________________R$25.000_____________________________\n"
              F"__________________para seu negócio_______________________\n"
              F"__________Pagando apenas com parcelas de sua alma________"
                  F""
                  F"\n__(S/N):")

        if a == "S" or a == "s":
            self.saldo = self.saldo + 25000
            return print(f"\nFechado Meu caro {self.nome}, Meu antro de enterna sofrimento lhe aguarda no fim de sua miseravel vida\nASS:Mochila de criança")

        if a == "N" or a == "n":
            print("\nA escolha é toda sua meu caro Forasteiro")
            return


    def mostrarSaldoAtual(self):
        print(f"O seu Saldo atual é {self.saldo}\n")
        return