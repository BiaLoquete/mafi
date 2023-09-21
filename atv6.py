import customtkinter as tk


tk.set_appearance_mode("dark")

janela = tk.CTk()
janela.title("Janela 1")
janela.geometry("400x350")
janela.configure(fg_color="grey31")
janela.resizable(width=False,height=False)
colunas = list(range(13))
linhas = list(range(13))
janela.grid_columnconfigure(colunas, weight=1)
janela.grid_rowconfigure(linhas, weight=1)

listprodutos = []
listaprecos = []

def adicionar():
    listprodutos.append(int(caixa1.get()))
    listaprecos.append(int(caixa2.get()))
    print(listprodutos)
    print(listaprecos)





texto= tk.CTkLabel(janela, text="Produtos")
texto.grid(row=6, column=6, columnspan=2)

caixa1=tk.CTkEntry(janela, placeholder_text="Digite o produto", width=120, height=50)
caixa1.grid(row=7, column=4, columnspan=2)

caixa2=tk.CTkEntry(janela, placeholder_text="Digite o preço", width=120, height=50)
caixa2.grid(row=7, column=7, columnspan=2)

btn1= tk.CTkButton(janela, text="Adicionar", command= adicionar, width=100, height=50, fg_color='DarkTurquoise')
btn1.grid (row=9, column=5)

btn2= tk.CTkButton(janela, text="Calcular", width=100, height=50, fg_color='DarkTurquoise')
btn2.grid (row=9, column=7)

texto1= tk.CTkLabel(janela, text="")
texto1.grid(row=10, column=6, columnspan=2)


janela.mainloop()