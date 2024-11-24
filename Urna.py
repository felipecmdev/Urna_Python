import csv
from CriarTela import *
from Eleitor import *
from Candidato import *

class Urna(CriarTela):
    eleitores = []
    candidatos = []
    cadastroRealizado : bool

    def __init__(self, root):
        self.cadastroRealizado = False
        super().__init__(root)
        self.voto = []
        eleitores = self.carregar_csv("Eleitores.csv")
        self.eleitores = [Eleitor(int(eleitor['Titulo']), eleitor['Nome'], eleitor['Municipio/UF'], eleitor['dataN']) for eleitor in eleitores]
        candidatos = self.carregar_csv("Candidatos.csv")
        self.candidatos = [Candidato(int(candidato['Numero']), candidato['Nome'], candidato['Cargo'], candidato['Vice']) for candidato in candidatos]

    def carregar_csv(self, arquivo):
        dados = []
        with open(arquivo, mode='r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)  
            for linha in leitor:
                dados.append(linha)
        return dados

    def botaoConfirma(self):
        if self.cadastroRealizado:
            if len(self.voto) == 2:
                self.label_resultado.config(text=f"Seu voto foi confirmado. Você digitou: {self.voto[0]}{self.voto[1]}")
                self.cadastroRealizado = False
            else:
                self.label_resultado.config(text="Voto inválido, digite dois números.")
                self.voto.clear()
        else:
         if len(self.voto) == 5:  
            titulo_digitado = int("".join(map(str, self.voto)))  
            eleitor_encontrado = next((eleitor for eleitor in self.eleitores if eleitor.Titulo == titulo_digitado), None)
        
            if eleitor_encontrado:
                self.label_resultado.config(
                    text=f"Eleitor encontrado:\n"
                        f"Nome: {eleitor_encontrado.Nome}\n"
                        f"Município/UF: {eleitor_encontrado.Municipio}\n"
                        f"Data de Nascimento: {eleitor_encontrado.DataN}\n"
                        "Você pode votar!")
                self.voto.clear()
                self.cadastroRealizado = True
            else:
                self.label_resultado.config(text="Título não encontrado. Digite novamente.")
                self.voto.clear()
         elif len(self.voto) < 5:
             self.label_resultado.config(text="Título não encontrado. Digite novamente.")
             self.voto.clear()
             

    def botaoBranco(self):
        print("Voto em branco")

    def botaoCorrigir(self):
        self.voto.clear()
        self.label_resultado.config(text="")

root = Tk()
app = Urna(root)
root.mainloop()