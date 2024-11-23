from tkinter import *
from tkinter import ttk
from Botoes import *

class CriarTela(Botoes):
    def __init__(self, root):                                                              
        self.root = root
        self.root.title("Urna Eletrônica")

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()

        self.label_titulo = ttk.Label(self.frm, text="Urna")
        self.label_titulo.grid(column=0, row=0, columnspan=3, pady=10)

        self.criarBotoes()

        self.label_resultado = ttk.Label(self.frm, text="")
        self.label_resultado.grid(column=0, row=7, columnspan=3, pady=10)