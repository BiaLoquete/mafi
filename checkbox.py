import customtkinter as Tk
from Modulo import*

janela = CriarJanelaP("Janela Principal", "400x400",1)

switch = CriarSwitch(janela, "lele",6,7)

janela.mainloop()