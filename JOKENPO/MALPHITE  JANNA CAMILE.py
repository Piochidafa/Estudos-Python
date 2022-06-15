import random

comp = random.randint(1, 3)

val = ""
valcomp = ""

usu = int(input("Insira sua resposta\n(1) - Pedra\n(2) - Papel\n(3) - Tesoura\n: - "))

if usu == 1:
    val = "Pedra"
elif usu == 2:
    val = "Papel"
elif usu == 3:
    val = "Tesoura"

elif usu != 1 or usu != 2 or usu != 3:
    print("Resposta invalida!!")

if comp == 1:
    valcomp = "Pedra"
elif comp == 2:
    valcomp = "Papel"
elif comp == 3:
    valcomp = "Tesoura"

if val == valcomp:
    print("\033[33mEmpate!!\033[m")

if val == "Pedra" and valcomp == "tesoura":
    print(f"Computador escolheu: \033[31m{valcomp}\033[m, \033[32mUsuário Ganhou !!\033[m ")

elif val == "Pedra" and valcomp == "Papel":
    print(f"Computador escolheu: \033[32m{valcomp}\033[m, \033[31mUsuário Perdeu !!\033[m ")

elif val == "Papel" and valcomp == "tesoura":
    print(f"Computador escolheu: \033[32m{valcomp}\033[m, \033[31mUsuário Perdeu !!\033[m ")

elif val == "Papel" and valcomp == "Pedra":
    print(f"Computador escolheu: \033[31m{valcomp}\033[m, \033[32mUsuário Ganhou !!\033[m ")

elif val == "Tesoura" and valcomp == "Pedra":
    print(f"Computador escolheu: \033[32m{valcomp}\033[m, \033[31mUsuário Perdeu !!\033[m")

elif val == "Tesoura" and valcomp == "Papel":
    print(f"Computador escolheu: \033[31m{valcomp}\033[m, \033[32mUsuário Ganhou !!\033[m ")



