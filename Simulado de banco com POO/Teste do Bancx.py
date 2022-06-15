
from Bancx import ClienteDoBanco

def limpar():
    print("\n")

Banco1 = ClienteDoBanco("Claudio", 2000)

Banco1.apresentacao()
limpar()

Banco1.efetuarCompra()
Banco1.mostrarSaldoAtual()
Banco1.efetuarCompra()
Banco1.mostrarSaldoAtual()

Banco1.emprestimo()


