import customtkinter as Tk
from Modulo import*

janela = CriarJanelaP("Janela Principal", "400x400",1)

slider = Tk.CTkSlider(janela, width=200, height=10)
slider.grid(row=12,column=6)
slider.get()

janela.mainloop()