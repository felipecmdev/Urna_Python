import csv
from CriarTela import *
from Eleitor import *
from Candidato import *

class Urna(CriarTela):
    eleitores = []
    candidatos = []

    def __init__(self, root):
        super().__init__(root)

        self.label_titulo = ttk.Label(self.frm, text="Urna")
        self.label_titulo.grid(column=0, row=0, columnspan=3, pady=10)
        eleitores = self.carregar_csv("Eleitores.csv")
        self.eleitores = [Eleitor(int(eleitor['Titulo']), eleitor['Nome'], eleitor['Municipio/UF'], eleitor['dataN']) for eleitor in eleitores]
        candidatos = self.carregar_csv("Candidatos.csv")
        self.candidatos = [Candidato(int(candidato['Numero']), candidato['Nome'], candidato['Cargo'], candidato['Vice']) for candidato in candidatos]

    def carregar_csv(self, arquivo):
        dados = []
        with open(arquivo, mode='r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)  # Usa o cabeçalho como chaves
            for linha in leitor:
                dados.append(linha)
        return dados

    def adicionarVoto(self, num):
        if len(self.voto) < 2:  
            self.voto.append(num)

    def botaoConfirma(self):
        if len(self.voto) == 2:
            self.label_resultado.config(text=f"Seu voto foi confirmado. Você digitou: {self.voto[0]}{self.voto[1]}")
        else:
            self.label_resultado.config(text="Voto inválido, digite dois números.")

    def botaoBranco(self):
        print("Voto em branco")

    def botaoCorrigir(self):
        self.voto.clear()
        self.label_resultado.config(text="Voto corrigido, digite novamente.")

root = Tk()
app = Urna(root)
root.mainloop()