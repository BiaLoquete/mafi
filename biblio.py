import customtkinter as Tk
Tk .set_appearance_mode ("System")



#criando uma janela
#instanciando uma classe para um objeto
#--> isso se chama ABSTRAÇÃO
janela = Tk .CTk()

#--> nome da janela
janela.title("Janela 1")

#--> para definir o tamanho da janela
#--> é em px
janela.geometry("400x350")

#cor da janela
janela.configure(fg_color="red")

#travar a janela, para ela não aumentar mais
janela.resizable(width=False, height=False)

#dividir a janela em quadradinhos, quadriculado
colunas = list (range(13))
linhas = list (range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

#criando um label
#o primeiro parâmetro é obrigatório ser o nome da janela
texto1= Tk.CTkLabel(janela, text="Digite...")
texto1.grid(row=6, column=6)
texto2= Tk .CTkLabel(janela, text="Digite...", text_color='blue', font=("Arial",15), justify="center")
texto2.grid(row=4, column=6)

#função do clique
def clicar():
    texto2.configure(text=caixa1.get())

#criando um botão
#o command é a função que o botão vai realizar
btn1= Tk.CTkButton(janela, text="Clique Aqui", command= clicar, width=100, height=30, fg_color='DarkTurquoise')
btn1.grid (row=8, column=6)

#criando uma caixa de texto
caixa1=Tk.CTkEntry(janela, placeholder_text="Digite seu nome", width=200, height=30)
caixa1.grid(row=7, column=6)
Texto=caixa1.get()


#--> para a janela ficar aparecendo . Tem que estar sempre no final
janela.mainloop()

