from tkinter import *
from tkinter import ttk

class Botoes():
    def __init__(self, root):
        self.root = root
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()

    def criarBotoes(self):
        ttk.Button(self.frm, text="Confirma", command=self.botaoConfirma).grid(column=2, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Branco", command=self.botaoBranco).grid(column=0, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Corrigir", command=self.botaoCorrigir).grid(column=1, row=6, padx=5, pady=5)


        botoes = [
        (1, 0, 0), (2, 1, 0), (3, 2, 0),
        (4, 0, 1), (5, 1, 1), (6, 2, 1),
        (7, 0, 2), (8, 1, 2), (9, 2, 2),
        (0, 1, 3)
    ]


        for num, col, row in botoes:
            ttk.Button(self.frm, text=str(num), command=lambda n=num: self.numeros(n)).grid(column=col, row=row, padx=5, pady=5)

    def numeros(self, n):
        self.voto.append(n)
        self.label_resultado.config(text=f"Você digitou: {''.join(map(str, self.voto))}")

    def botaoConfirma(self):
        pass

    def botaoBranco(self):
        pass

    def botaoCorrigir(self):
        pass