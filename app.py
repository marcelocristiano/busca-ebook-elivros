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
dados = [
    ['Marcelo', 'Livro1', "https://www.google.com/"],
    ['João', 'Livro2', "https://www.example.com/"],
    ['Maria', 'Livro3', "https://www.python.org/"],
    ['Ana', 'Livro4', "https://www.wikipedia.org/"],
    ['Pedro', 'Livro5', "https://www.github.com/"],
    ['Carlos', 'Livro6', "https://www.stackoverflow.com/"],
    ['Juliana', 'Livro7', "https://www.openai.com/"],
    ['Fernanda', 'Livro8', "https://www.microsoft.com/"],
    ['Rafael', 'Livro9', "https://www.apple.com/"]
]

# Adiciona uma ligação de clique à tag "hyperlink"
t_livro.tag_bind("hyperlink", "<Button-1>", abrir_link)

# Inicia o loop principal da aplicação
app.mainloop()