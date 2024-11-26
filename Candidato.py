# Classe que define atributos para os candidatos
class Candidato:
    Numero : int
    Nome : str
    Votos : int
    Cargo : str
    Vice : str

# Método construtor, que inicializa as propriedades do candidato
    def __init__(self, numero, nome, cargo, vice):
        self.Numero = numero
        self.Nome = nome
        self.Votos = 0
        self.Cargo = cargo
        self.Vice = vice

# Método para registrar um voto no candidato
    def registrarVoto(self):
        self.Votos += 1

# Método especial para retornar uma representação em string do objeto
    def __str__(self):
        return f'{self.Numero} - {self.Nome}'
        