import requests
from bs4 import BeautifulSoup

# Cria variavel para armazenar a URL do site a ser raspado
url = 'https://elivros.love/Search/augusto-cury'
def pesquisar(url):
    # Executa a requisição ao site e armazena o retorno na variavel
    resp = requests.get(url)
    # Trasforma o objeto de resposta em html mais legivel
    soup = BeautifulSoup(resp.text, 'html.parser')
    return soup


def buscar_paginas(soup):
    links_paginas = []
    paginas = soup.find_all(class_='page-link')
    for pagina in paginas[1:]:
        links_paginas.append(pagina['href'].strip())
    return links_paginas

def buscar_livro(links_paginas: list):
    livros = []
    for link_pagina in links_paginas:
        # Executa a requisição ao site e armazena o retorno na variavel
        resp = requests.get(link_pagina)

        # Trasforma o objeto de resposta em html mais legivel
        soup_pagina = BeautifulSoup(resp.text, 'html.parser')

        class_livros = soup_pagina.find_all(class_="bInfo")

        for info_livro in class_livros:
            autor = info_livro.find(class_="autor").text.strip()
            titulo = info_livro.find('a').text.strip()
            link = 'https:' + info_livro.find('a')['href']
            livros.append([autor, titulo, link])
    
        #livros = sorted(livros, key=lambda x: x[0])
    return livros
