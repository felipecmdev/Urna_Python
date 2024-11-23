class Candidato:
    numero : int
    nome : str
    votos : int
    cargo : str
    vice : str

    def __init__(self, numero, nome, cargo, vice):
        self.numero = numero
        self.nome = nome
        self.votos = 0
        self.cargo = cargo
        self.vice = vice

    def registrarVoto(self):
        self.votos += 1

    def __str__(self):
        return f'{self.numero} - {self.nome}'
        