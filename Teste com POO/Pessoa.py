
class Pessoa:

    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def Ano_de_nascimento(self):
        print(f"{self.nome} O seu ano de nascimento é {self.ano_atual - self.idade}, acertei?!")








