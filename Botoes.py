from tkinter import *
from tkinter import ttk

#Classe para a criação dos botões da urna
class Botoes():
    def __init__(self, root):
        self.root = root
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()

# Método que cria os botões e define os comandos associados
    def criarBotoes(self):
        # Botões: "Confirma", "Branco" e "Corrigir"
        ttk.Button(self.frm, text="Confirma", command=self.botaoConfirma).grid(column=2, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Branco", command=self.botaoBranco).grid(column=0, row=6, padx=5, pady=5)
        ttk.Button(self.frm, text="Corrigir", command=self.botaoCorrigir).grid(column=1, row=6, padx=5, pady=5)

        # Botões numéricos dispostos em uma matriz 3x3 e um botão adicional para o número "0"
        botoes = [
        (1, 0, 0), (2, 1, 0), (3, 2, 0),
        (4, 0, 1), (5, 1, 1), (6, 2, 1),
        (7, 0, 2), (8, 1, 2), (9, 2, 2),
        (0, 1, 3)
    ]

        # Cria os botões numéricos e associa a função 'numeros' ao comando de cada botão
        for num, col, row in botoes:
            ttk.Button(self.frm, text=str(num), command=lambda n=num: self.numeros(n)).grid(column=col, row=row, padx=5, pady=5)

# Métodos que definem o comportamento dos botões
    def numeros(self, n):
        self.voto.append(n)
        self.label_resultado.config(text=f"Você digitou: {''.join(map(str, self.voto))}")
        self.botaoPressionado()
    
    def botaoPressionado(self, numero):
        pass

    def botaoConfirma(self):
        pass

    def botaoBranco(self):
        pass

    def botaoCorrigir(self):
        pass