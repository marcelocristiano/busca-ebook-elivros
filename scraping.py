import requests
from bs4 import BeautifulSoup


def buscar_livro(url):
    #Executa a requisição ao site e armazena o retorno na variavel
    resp = requests.get(url)

    # Trasforma o objeto de resposta em html mais legivel
    soup = BeautifulSoup(resp.text, 'html.parser')

    num_page = soup.find(class_="pgNumbers").find_all('b')[1].text
    num_page = int(num_page)+1

    livros = []
    for num in range(1, num_page + 1):
        # Executa a requisição ao site e armazena o retorno na variavel
        resp = requests.get(url + '/' + str(num))

        # Trasforma o objeto de resposta em html mais legivel
        soup_pagina = BeautifulSoup(resp.text, 'html.parser')

        class_livros = soup_pagina.find_all(class_="bInfo")

        for info_livro in class_livros:
            autor = info_livro.find(class_="autor").text.strip()
            titulo = info_livro.find('a').text.strip()
            link = 'https:' + info_livro.find('a')['href']
            livros.append([autor, titulo, link])
    
    livros = sorted(livros, key=lambda x: x[0])
    return livros