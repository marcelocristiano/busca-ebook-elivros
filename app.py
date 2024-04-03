import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import scraping
import time
import webbrowser  # Importa o módulo para abrir URLs

app = ttk.Window('Buscar Livros')
app.geometry('1200x900')
app.iconbitmap('img\e-book.ico')
app.resizable(width=False, height=False)
style = Style(theme='superhero')

l_titulo = ttk.Label(app, text="Buscar Livros")
l_titulo.pack(padx=0, pady=10)
l_titulo.config(font=("Arial", 25,'bold'))

l_titulo_2 = ttk.Label(app, text="elivros.love")
l_titulo_2.pack(padx=10, pady=0)
l_titulo_2.config(font=("Arial", 11, 'italic'))

f_entry_busca = ttk.Frame(app, border=1)
f_entry_busca.pack(padx=10, pady=30)

e_busca = ttk.Entry(f_entry_busca, width=48)          
e_busca.focus_set()
e_busca.grid(column=0, row=0, padx=10)

def teste():
    t_livro.delete(*t_livro.get_children())
    num = 0
    maximo = len(dados)

    for dado in dados:
        barra_progresso['maximum'] = maximo
        t_livro.insert('', END, values=dado)
        barra_progresso['value'] = num + 1
        app.update_idletasks()
        time.sleep(1)
        num = num + 1

# Função para abrir o link no navegador padrão
def abrir_link(event):
    item = t_livro.selection()[0]
    link = t_livro.item(item, "values")[2]  # Obtém o link da terceira coluna
    webbrowser.open_new(link)

btn_buscar= ttk.Button(f_entry_busca, text='Buscar', width=10, command=teste)
btn_buscar.grid(column=1, row=0)

# Cria uma barra de progresso
barra_progresso = ttk.Progressbar(bootstyle="warning", length=800)
barra_progresso.pack()

# Define as colunas da tabela de resultados
colunas = ['Autor', 'Livro', 'Download']

# Cria a tabela para exibir os resultados da busca
t_livro = ttk.Treeview(app, columns=colunas, show='headings', bootstyle='primary')
t_livro.place(x=100, y=260, width=1000, height=560)  # Posiciona a tabela na janela principal
t_livro.heading('Autor', text='Autor')  # Define o cabeçalho da coluna 'Autor'
t_livro.heading('Livro', text='Livro')  # Define o cabeçalho da coluna 'Livro'
t_livro.heading('Download', text='Download')  # Define o cabeçalho da coluna 'Download'

# Vincula o evento de clique duplo à função abrir_link
t_livro.bind("<Double-1>", abrir_link)

# Insere dados de exemplo na tabela
dados = livros = [
    ['Auguste Comte', 'Curso de Filosofia Positiva, Discurso Sobre o Espírito Positivo', 'https://elivros.love/livro/baixar-livro-curso-de-filosofia-positiva-discurso-sobre-o-espirito-positivo-auguste-comte-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'Ansiedade - Como Enfrentar o Mal do Século', 'https://elivros.love/livro/baixar-livro-ansiedade-como-enfrentar-o-mal-do-seculo-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'Ansiedade 3: Ciúme', 'https://elivros.love/livro/baixar-livro-ansiedade-3-ciume-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'Armadilhas da Mente', 'https://elivros.love/livro/baixar-livro-armadilhas-da-mente-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'A Fascinante Construção do Eu', 'https://elivros.love/livro/baixar-livro-fascinante-construcao-do-eu-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'Em Busca do Sentido da Vida', 'https://elivros.love/livro/baixar-livro-em-busca-do-sentido-da-vida-augusto-cury-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'Nunca Desista dos Seus Sonhos', 'https://elivros.love/livro/baixar-livro-nunca-desista-dos-seus-sonhos-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Augusto Cury', 'O Colecionador de Lágrimas', 'https://elivros.love/livro/baixar-livro-o-colecionador-de-lágrimas-augusto-cury-em-epub-pdf-mobi-ou-ler-online'],
    ['Carlos Augusto de Proença Rosa', 'História da Ciência: Da Antiguidade ao Renascimento Científico', 'https://elivros.love/livro/baixar-livro-historia-da-ciencia-da-antiguidade-ao-renascimento-cientifico-carlos-augusto-de-proenca-rosa-em-epub-pdf-mobi-ou-ler-online'],
    ['Carlos Augusto Lopes Filho', 'Os Desbravadores', 'https://elivros.love/livro/baixar-livro-os-desbravadores-carlos-augusto-lopes-filho-em-epub-pdf-mobi-ou-ler-online'],
    ['Cissa Guimarães', 'Viver Com Fé - Histórias de Quem Acredita', 'https://elivros.love/livro/baixar-viver-com-fe-historias-de-quem-acredita-cissa-guimaraes-epub-pdf-mobi-ou-ler-online'],
    ['Daniel Coyle', 'Equipes Brilhantes: Como Criar Grupos Fortes e Motivados', 'https://elivros.love/livro/baixar-livro-equipes-brilhantes-como-criar-grupos-fortes-e-motivados-daniel-coyle-em-epub-pdf-mobi-ou-ler-online'],
    ['Denise Assis', 'Claudio Guerra: Matar e Queimar', 'https://elivros.love/livro/baixar-livro-claudio-guerra-matar-queimar-denise-assis-em-epub-pdf-mobi-ou-ler-online'],
    ['Flávio Augusto da Silva', 'Ponto de Inflexão', 'https://elivros.love/livro/baixar-livro-ponto-de-inflexao-flavio-augusto-da-silva-em-epub-pdf-mobi-ou-ler-online'],
    ['George Orwell', 'O que é Fascismo? e Outros Ensaios', 'https://elivros.love/livro/baixar-livro-o-que-e-fascismo-e-outros-ensaios-george-orwell-em-epub-pdf-mobi-ou-ler-online'],
    ['Henrique Schneider', 'A Solidão do Amanhã', 'https://elivros.love/livro/baixar-livro-solidao-do-amanha-henrique-schneider-em-epub-pdf-mobi-ou-ler-online'],
    ['Hermann Broch', 'A Morte de Virgílio', 'https://elivros.love/livro/baixar-livro-morte-de-virgilio-hermann-broch-em-epub-pdf-mobi-ou-ler-online'],
    ['Ivan Bichara', 'Carcará', 'https://elivros.love/livro/baixar-livro-carcara-ivan-bichara-em-epub-pdf-mobi-ou-ler-online'],
    ['Jas Silva', 'O Barão do Café', 'https://elivros.love/livro/baixar-livro-o-barao-do-cafe-jas-silva-em-epub-pdf-mobi-ou-ler-online'],
    ['João Guimarães Rosa', 'A Hora e Vez de Augusto Matraga', 'https://elivros.love/livro/baixar-livro-a-hora-e-vez-de-augusto-matraga-joao-guimaraes-rosa-em-epub-pdf-mobi-ou-ler-online'],
    ['João Guimarães Rosa', 'Sagarana', 'https://elivros.love/livro/baixar-livro-sagarana-joao-guimaraes-rosa-em-epub-pdf-mobi-ou-ler-online'],
    ['Joaquim Campelo Marques', 'História da Literatura Ocidental', 'https://elivros.love/livro/baixar-livro-historia-da-literatura-ocidental-joaquim-campelo-marques-em-epub-pdf-mobi-ou-ler-online'],
    ['Jose Augusto Minarelli', 'Superdicas de Networking para sua vida Pessoal e Profissional', 'https://elivros.love/livro/baixar-livro-superdicas-de-networking-para-sua-vida-pessoal-profissional-jose-augusto-minarelli-em-epub-pdf-mobi-ou-ler-online'],
    ['Luís Augusto Fischer', 'Dicionário de Porto-Alegrês', 'https://elivros.love/livro/baixar-livro-dicionario-de-porto-alegres-luis-augusto-fischer-em-epub-pdf-mobi-ou-ler-online'],
    ['Luiz Alberto Moniz Bandeira', 'Fórmula para o Caos', 'https://elivros.love/livro/baixar-livro-formula-para-caos-luiz-alberto-moniz-bandeira-em-epub-pdf-mobi-ou-ler-online'],
    ['Marco Lucchesi', 'O Bibliotecário do Imperador', 'https://elivros.love/livro/baixar-o-bibliotecario-do-imperador-marco-lucchesi-epub-pdf-mobi-ou-ler-online'],
    ['Mary Del Priore', 'O Príncipe Maldito', 'https://elivros.love/livro/baixar-o-principe-maldito-mary-del-priore-epub-pdf-mobi-ou-ler-online'],
    ['Nísia Floresta', 'Fany ou o Modelo das Donzelas', 'https://elivros.love/livro/baixar-livro-fany-ou-modelo-das-donzelas-nisia-floresta-em-epub-pdf-mobi-ou-ler-online'],
    ['Olivier Besancenot', 'Setembro Vermelho: O Golpe de Estado no Chile em 1973', 'https://elivros.love/livro/baixar-livro-setembro-vermelho-golpe-de-estado-no-chile-em-1973-olivier-besancenot-em-epub-pdf-mobi-ou-ler-online'],
    ['Ricardo Seitenfus', 'Manual das Organizações Internacionais', 'https://elivros.love/livro/baixar-livro-manual-das-organizacoes-internacionais-ricardo-seitenfus-em-epub-pdf-mobi-ou-ler-online'],
    ['Rogerio Augusto Schmitt', 'Partidos Políticos No Brasil (1945-2000)', 'https://elivros.love/livro/baixar-livro-partidos-politicos-no-brasil-1945-2000-rogerio-augusto-schmitt-em-epub-pdf-mobi-ou-ler-online'],
    ['Rubem Fonseca', 'Mandrake: A Bíblia e a Bengala', 'https://elivros.love/livro/baixar-livro-mandrake-biblia-bengala-rubem-fonseca-em-epub-pdf-mobi-ou-ler-online'],
    ['Rubem Fonseca', 'Os Prisioneiros Rubem Fonseca', 'https://elivros.love/livro/baixar-os-prisioneiros-rubem-fonseca-rubem-fonseca-epub-pdf-mobi-ou-ler-online'],
    ['R. Augusto', 'Imunologia Fundamental: Medbook', 'https://elivros.love/livro/baixar-livro-imunologia-fundamental-medbook-r-augusto-em-epub-pdf-mobi-ou-ler-online'],
    ['Roosevelt Augusto', 'O Fraseador', 'https://elivros.love/livro/baixar-livro-o-fraseador-roosevelt-augusto-em-epub-pdf-mobi-ou-ler-online'],
    ['Sérgio Sant’Anna', 'Páginas Sem Glória', 'https://elivros.love/livro/baixar-paginas-sem-gloria-sergio-santanna-epub-pdf-mobi-ou-ler-online'],
    ['Sergio Augusto de Avellar Coutinho', 'A Revolução Gramscista No Ocidente', 'https://elivros.love/livro/baixar-livro-a-revolucao-gramscista-no-ocidente-sergio-augusto-de-avellar-coutinho-em-epub-pdf-mobi-ou-ler-online'],
    ['Vinicius de Moraes', '50 Poemas Macabros', 'https://elivros.love/livro/baixar-livro-50-poemas-macabros-vinicius-de-moraes-em-epub-pdf-mobi-ou-ler-online'],
    ['William Shakespeare', 'Antônio e Cleópatra', 'https://elivros.love/livro/baixar-antonio-e-cleopatra-william-shakespeare-epub-pdf-mobi-ou-ler-online'],
    ['Conn Iggulden', 'Sangue dos Deuses', 'https://elivros.love/livro/baixar-livro-sangue-dos-deuses-o-imperador-vol-5-conn-iggulden-em-epub-pdf-mobi-ou-ler-online']
]


# Adiciona uma ligação de clique à tag "hyperlink"
t_livro.tag_bind("hyperlink", "<Button-1>", abrir_link)

# Inicia o loop principal da aplicação
app.mainloop()