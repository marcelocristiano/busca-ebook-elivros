import requests
from bs4 import BeautifulSoup

# Cria variavel para armazenar a URL do site a ser raspado
url = 'http://lelivros.love/'

# Executa a requisição ao site e armazena o retorno na variavel
resp = requests.get(url)

# Trasforma o objeto de resposta em html mais legivel
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)