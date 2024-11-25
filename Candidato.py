class Candidato:
    Numero : int
    Nome : str
    Votos : int
    Cargo : str
    Vice : str

    def __init__(self, numero, nome, cargo, vice):
        self.Numero = numero
        self.Nome = nome
        self.Votos = 0
        self.Cargo = cargo
        self.Vice = vice

    def registrarVoto(self):
        self.Votos += 1

    def __str__(self):
        return f'{self.Numero} - {self.Nome}'
        