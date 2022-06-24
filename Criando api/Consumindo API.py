import requests


apiminha = requests.get("http://127.0.0.1:5000/")
app = requests.get("http://viacep.com.br/ws/78099160/json/")

conteudo = apiminha.json()
cont = app.json()

print(type(conteudo))
print(conteudo['p1']['firstName'])
print(type(cont))
print(cont['bairro'])


# for i in conteudos:
#     print(i)