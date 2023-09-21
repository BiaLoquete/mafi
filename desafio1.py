import customtkinter as Tk
Tk .set_appearance_mode ("System")

janela = Tk .CTk()

#--> nome da janela
janela.title("Janela 1")

#--> para definir o tamanho da janela
#--> é em px
janela.geometry("400x350")

#travar a janela, para ela não aumentar mais
janela.resizable(width=False, height=False)

#dividir a janela em quadradinhos, quadriculado
colunas = list (range(13))
linhas = list (range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)


def verificar():
    n1 = int(caixa1.get())
    n2 = int(caixa2.get())

    if n1 < n2:
        texto1.configure(text="O segundo número é maior")
    elif n1 > n2:
        texto1.configure(text="O primeiro número é maior")
    else:
        texto1.configure(text="São iguais")

texto1= Tk.CTkLabel(janela, text="Digite...")
texto1.grid(row=6, column=6)

#criando uma caixa de texto
caixa1=Tk.CTkEntry(janela, placeholder_text="Digite um número", width=200, height=30)
caixa1.grid(row=7, column=6)

#criando uma caixa de texto
caixa2=Tk.CTkEntry(janela, placeholder_text="Digite outro número", width=200, height=30)
caixa2.grid(row=8, column=6)

#criando um botão
#o command é a função que o botão vai realizar
btn1= Tk.CTkButton(janela, text="Clique Aqui", command= verificar, width=100, height=30, fg_color='DarkTurquoise')
btn1.grid (row=9, column=6)


janela.mainloop()