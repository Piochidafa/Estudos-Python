import requests
from bs4 import BeautifulSoup

# Requisitando para o servidor referente ao url *1
# Transformando o conteudo da pagina em html *2
# Passando em forma de dicionario os caminhos(a classe e o valor que tem na classe) *3
# Encontrando tudo que tem dentro da div com os valores do dicionario *4
#  Printando os valores encontrados nesse caminho com o .text *5

# Cores para deixar tudo mais frufru
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

i = 0

''' *1 '''
url = 'https://store.steampowered.com/specials#tab=TopSellers'
page = requests.get(url)

''' *2 '''

soup = BeautifulSoup(page.content, 'html.parser')

''' *3 '''

atributos = {'class':'tab_item_name'}
valores = {'class':'discount_final_price'}


''' *4 '''

dados_obtidos = soup.find_all("div", attrs=atributos)
valores = soup.find_all("div", attrs=valores)


''' *5 '''

while i < 10:
    print(f"{REVERSE}{dados_obtidos[i].text}{RESET} \nvalor:{GREEN} {valores[i].text}{RESET}\n")
    i+=1

