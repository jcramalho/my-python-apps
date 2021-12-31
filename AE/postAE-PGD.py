import requests
import urllib3
import json

# Pedido para fazer a autenticação do utilizador e obter o token:
print("Vou fazer a autenticação:...")
url = 'http://clav-api.di.uminho.pt/v2/users/login'
myobj = {'username': 'jcr@di.uminho.pt', 'password': '123'}
x = requests.post(url, data = myobj)
user = json.loads(x.text)
token = user['token']
print('Utilizador ' + user['name'] + " autenticado.")

# Envio de um AE
print("Vou enviar um AE:...")
url2 = 'http://clav-api.di.uminho.pt/v2/autosEliminacao/importar?tipo=PGD&token=' + token
ae = open("AE-IMT.xml")
conteudo = ae.read()
http = urllib3.PoolManager()
resp = http.request(
    "POST",
    url2,
    fields= {
       "file": ("AE-FCT.xml", conteudo, "text/xml"),
    }
)

print(json.loads(resp.data))