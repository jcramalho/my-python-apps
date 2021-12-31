import requests
import json

# Pedido para fazer a autenticação do utilizador e obter o token:
print("Vou fazer a autenticação:...")
url = 'http://clav-api.di.uminho.pt/v2/users/login'
myobj = {'username': 'jcr@di.uminho.pt', 'password': '123'}
x = requests.post(url, data = myobj)
user = json.loads(x.text)
token = user['token']
print('Utilizador ' + user['name'] + " autenticado.")

# Pedido da lista de tipologias
print("Vou pedir a lista de tipologias:...")
url2 = 'http://clav-api.di.uminho.pt/v2/tipologias?token=' + token
y = requests.get(url2)
tip = json.loads(y.text)
print("Recebi " + str(len(tip)) + " tipologias.")
# for t in tip:
#    print("|".join(t))