import pyautogui

def menu():
 a = (pyautogui.confirm(text='|-------------------------------------------|  \n'
                              '|  <1>- Adição                              |       \n'
                              '|  <2>- Subtração                        |       \n'
                              '|  <3>- Multiplicação                    |\n'
                              '|  <4>- Divisão                              |\n'
                              '|________________________|                 \n',
                         buttons=['Adição', 'Subtração', 'Divisão', 'Multiplicação']))
 return a

def resultado_da_conta(x, y):
      if menu() == "Adição":
            c = x + y
      elif menu() == "Subtração":
            c = x - y
      elif menu() == "Multiplicação":
            c = x * y
      elif menu() == "Divisão":
            c = x/y

      return c


def Numero1():
 a = int(pyautogui.prompt(text='Digite o primeiro Numero', title='^_____^', default=''))


 return a

def Numero2():
    b = int(pyautogui.prompt(text='Digite o segundo Numero', title='^_____^', default=''))

    return b


funcao = pyautogui.confirm(text="Escolha a Função desejada", title="Canivete suiço dos brabo", buttons=['Calculadora',
                                                                                                   'Outra Coisa',
                                                                                                   'Outra Outra Coisa'])
if funcao == "Calculadora":
    a = Numero1()
    b = Numero2()
    g = resultado_da_conta(a,b)
    pyautogui.alert(text=f" o Resultado é {g} ", title='Resultado')



# senha = (pyautogui.password(text='Coloque a senha', title='Senha teste', default='Frangaralho', mask="*"))











