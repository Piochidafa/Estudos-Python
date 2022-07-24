import requests

url = 'https://viacep.com.br/ws/01001000/json/'

a = requests.get(url=url)

print(a.status_code)