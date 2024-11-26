import csv
from CriarTela import *
from Eleitor import *
from Candidato import *
import os
import pickle

# Classe que representa a urna eletrônica e suas funcionalidades
class Urna(CriarTela):
    eleitores = []
    candidatos = []
    votoBranco : int

#Construtor da classe Urna, inicializa a interface gráfica e carrega os dados dos eleitores e candidatos.
    def __init__(self, root):
        self.cadastroRealizado = False
        super().__init__(root)
        self.votoBranco = 0
        ttk.Button(self.frm, text="Exibir Resultados", command=self.exibirResultados).grid(column=0, row=9, columnspan=3, pady=10)
        self.voto = []
        eleitores = self.carregar_csv("Eleitores.csv")
        self.eleitores = [Eleitor(int(eleitor['Titulo']), eleitor['Nome'], eleitor['Municipio/UF'], eleitor['dataN']) for eleitor in eleitores]
        candidatos = self.carregar_csv("Candidatos.csv")
        self.candidatos = [Candidato(int(candidato['Numero']), candidato['Nome'], candidato['Cargo'], candidato['Vice']) for candidato in candidatos]

# Método que lê os dados de um arquivo CSV e retorna uma lista de dicionários com os dados
    def carregar_csv(self, arquivo):
        dados = []
        with open(arquivo, mode='r', encoding='utf-8') as csvfile:
            leitor = csv.DictReader(csvfile)  
            for linha in leitor:
                dados.append(linha)
        return dados
    
# Método para exibir informações de um candidato baseado no número digitado  
    def candidatoInfo(self):
        votoDigitado = int("".join(map(str, self.voto)))  
        candidato_encontrado = next((candidato for candidato in self.candidatos if candidato.Numero == votoDigitado), None)
        if candidato_encontrado:
            self.label_resultado.config(
                text=f"candidato encontrado:\n"
                    f"Nome: {candidato_encontrado.Nome}\n"
                    f"Número: {candidato_encontrado.Numero}\n"
                    f"Cargo: {candidato_encontrado.Cargo}\n"
                    f"Vice: {candidato_encontrado.Vice}\n")
        else: 
            self.label_resultado.config(text="Candidato não encontrado. Digite novamente.")
            self.voto.clear()

# Método de verificação e autenticação do título de eleitor digitado
    def eleitorInfo(self):
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
        else:
             self.label_resultado.config(text="Título precisa ter 5 números. Digite novamente.")
             self.voto.clear()
 
# Realiza ações quando um botão numérico é pressionado
    def botaoPressionado(self):
        if self.cadastroRealizado:
            if len(self.voto) == 2:
                self.candidatoInfo()            

# Confirma o voto e registra o candidato escolhido
    def botaoConfirma(self):
        if self.cadastroRealizado:
            if len(self.voto) == 2:
                votoDigitado = int("".join(map(str, self.voto))) 
                candidato_encontrado = next((c for c in self.candidatos if c.Numero == votoDigitado), None)
                
                if candidato_encontrado:
                    candidato_encontrado.registrarVoto()
                    self.label_resultado.config(
                        text=f"Seu voto foi confirmado!\n"
                            f"Você votou no candidato {candidato_encontrado.Nome}."
                    )
                    self.salvarVoto(votoDigitado)
                    self.voto.clear()
                    self.cadastroRealizado = False
                else:
                    self.label_resultado.config(text="Candidato não encontrado. Voto inválido.")
                
                self.voto.clear()
                self.cadastroRealizado = False
            else:
                self.label_resultado.config(text="Voto inválido, digite dois números.")
                self.voto.clear()
        else:
            self.eleitorInfo()

# Salva o voto em um arquivo utilizando pickle
    def salvarVoto(self, voto):
        pasta_documentos = os.path.expanduser("~/Documents")
        caminho_arquivo = os.path.join(pasta_documentos, "votos.pckl")

        if not os.path.exists(pasta_documentos):
            os.makedirs(pasta_documentos)

        dados_votos = {"votos": [], "votos_brancos": 0}

        try:
            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, "rb") as arquivo:
                    dados_votos = pickle.load(arquivo)
                    if isinstance(dados_votos, list):
                        dados_votos = {"votos": dados_votos, "votos_brancos": 0}
        except (EOFError, pickle.UnpicklingError):
            pass

        if voto == "branco":
            dados_votos["votos_brancos"] = self.votoBranco  
        else:
            dados_votos["votos"].append(voto)

        with open(caminho_arquivo, "wb") as arquivo:
            pickle.dump(dados_votos, arquivo)

        print(f"Voto salvo com sucesso em {caminho_arquivo}")

# Método para exibir os resultados da votação
    def exibirResultados(self):
        pasta_documentos = os.path.expanduser("~/Documents")
        caminho_arquivo = os.path.join(pasta_documentos, "votos.pckl")

        if not os.path.exists(caminho_arquivo):
            self.label_resultado.config(text="Nenhum voto foi registrado ainda.")
            return

        try:
            with open(caminho_arquivo, "rb") as arquivo:
                dados_votos = pickle.load(arquivo)
                if isinstance(dados_votos, list):
                    dados_votos = {"votos": dados_votos, "votos_brancos": 0}
        except (EOFError, pickle.UnpicklingError):
            self.label_resultado.config(text="Erro ao carregar os votos.")
            return

        votos = dados_votos.get("votos", [])
        self.votoBranco = dados_votos.get("votos_brancos", 0)  

        votos_por_candidato = {}
        for voto in votos:
            if voto in votos_por_candidato:
                votos_por_candidato[voto] += 1
            else:
                votos_por_candidato[voto] = 1

        resultados = "Resultados da votação:\n"
        for candidato in self.candidatos:
            numero = candidato.Numero
            nome = candidato.Nome
            votos_candidato = votos_por_candidato.get(numero, 0)
            resultados += f"{nome} ({numero}): {votos_candidato} voto(s)\n"

        resultados += f"Votos em branco: {self.votoBranco}\n"
        self.label_resultado.config(text=resultados)


             
# Método para registrar um voto em branco
    def botaoBranco(self):
        if self.cadastroRealizado:
            self.votoBranco += 1
            self.salvarVoto("branco")
            self.label_resultado.config(text="Você votou em branco.")
        else: 
            self.label_resultado.config(text="Título não encontrado. Digite novamente.") 
        self.cadastroRealizado = False 

# Limpa o voto digitado
    def botaoCorrigir(self):
        self.voto.clear()
        self.label_resultado.config(text="")

# Configura a aplicação Tkinter
root = Tk()
app = Urna(root)
root.mainloop()