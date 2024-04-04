import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import scraping
import webbrowser  # Importa o módulo para abrir URLs

app = ttk.Window('Buscar Livros')
app.geometry('1000x700')
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
f_entry_busca.pack(padx=10, pady=20)

e_busca = ttk.Entry(f_entry_busca, width=48)          
e_busca.focus_set()
e_busca.grid(column=0, row=0, padx=10)

l_buscando_livros = ttk.Label(text='', font=("Arial", 13, 'italic'))
l_buscando_livros.pack(pady=10)

def scraping_dados():
    t_livro.delete(*t_livro.get_children())

    texo_pesquisa = str(e_busca.get().replace(' ', '-'))

    l_buscando_livros['text'] = 'Buscando Livros...  '
    app.update_idletasks()

    dados = scraping.buscar_livro('https://elivros.love/Search/' + texo_pesquisa)
    maximo = len(dados)

    l_buscando_livros['text'] = str(maximo) + ' Livros Econtrados'

    num = 0
    
    for dado in dados:
        t_livro.insert('', END, values=dado)
        app.update_idletasks()
        num = num + 1

# Função para abrir o link no navegador padrão
def abrir_link(event):
    item = t_livro.selection()[0]
    link = t_livro.item(item, "values")[2]  # Obtém o link da terceira coluna
    webbrowser.open_new(link)

btn_buscar= ttk.Button(f_entry_busca, text='Buscar', width=10, command=scraping_dados)
btn_buscar.grid(column=1, row=0)

# Define as colunas da tabela de resultados
colunas = ['Autor', 'Livro', 'Download']

# Cria a tabela para exibir os resultados da busca
t_livro = ttk.Treeview(app, columns=colunas, show='headings', bootstyle='primary')
t_livro.place(relx=0.05, rely=0.30, relwidth=0.90, relheight=0.60)
#t_livro.pack(padx=50, pady=20, fill='both', side='top', )  # Posiciona a tabela na janela principal
t_livro.heading('Autor', text='Autor')  # Define o cabeçalho da coluna 'Autor'
t_livro.heading('Livro', text='Livro')  # Define o cabeçalho da coluna 'Livro'
t_livro.heading('Download', text='Download')  # Define o cabeçalho da coluna 'Download'

# Vincula o evento de clique duplo à função abrir_link
t_livro.bind("<Double-1>", abrir_link)

# Adiciona uma ligação de clique à tag "hyperlink"
t_livro.tag_bind("hyperlink", "<Button-1>", abrir_link)

# Inicia o loop principal da aplicação
app.mainloop()