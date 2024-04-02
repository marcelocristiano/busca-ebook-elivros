import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import scraping



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

f_entry_busca = ttk.Frame(app)
f_entry_busca.pack(padx=10, pady=30)

e_busca = ttk.Entry(f_entry_busca, width=48)          
e_busca.focus_set()
e_busca.grid(column=0, row=0, padx=10)

btn_buscar= ttk.Button(f_entry_busca, text='Buscar', width=10, command=scraping.buscar_livro)
btn_buscar.grid(column=1, row=0)




app.mainloop()