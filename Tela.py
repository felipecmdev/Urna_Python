from tkinter import *
from tkinter import ttk

class UrnaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Urna Eletrônica")
        
        self.voto = []

        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()

        self.label_titulo = ttk.Label(self.frm, text="Urna")
        self.label_titulo.grid(column=0, row=0, columnspan=3, pady=10)

        self.criarBotoes()

        self.label_resultado = ttk.Label(self.frm, text="")
        self.label_resultado.grid(column=0, row=7, columnspan=3, pady=10)

    def criarBotoes(self):
        ttk.Button(self.frm, text="Confirma", command=self.votoConfirmado).grid(column=2, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Branco", command=self.voto_branco).grid(column=0, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Corrigir", command=self.votoCorrigir).grid(column=1, row=6, padx=5, pady=5)

        # Botões de números
        botoes = [
            (7, 0, 0), (4, 1, 0), (1, 2, 0),
            (8, 0, 1), (5, 1, 1), (2, 2, 1),
            (9, 0, 2), (6, 1, 2), (3, 2, 2),
            (0, 1, 3)
        ]

        for num, col, row in botoes:
            ttk.Button(self.frm, text=str(num), command=lambda n=num: self.adcionarVoto(n)).grid(column=col, row=row, padx=5, pady=5)

    def adcionarVoto(self, num):
        if len(self.voto) < 2:  
            self.voto.append(num)

    def votoConfirmado(self):
        if len(self.voto) == 2:
            self.label_resultado.config(text=f"Seu voto foi confirmado. Você digitou: {self.voto[0]}{self.voto[1]}")
        else:
            self.label_resultado.config(text="Voto inválido, digite dois números.")

    def voto_branco(self):
        print("Voto em branco")

    def votoCorrigir(self):
        self.voto.clear()
        self.label_resultado.config(text="Voto corrigido, digite novamente.")

root = Tk()
app = UrnaApp(root)
root.mainloop()