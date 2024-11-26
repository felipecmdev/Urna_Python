# Classe que define atributos para os Eleitores
class Eleitor():
    Titulo : int
    Nome : str
    Municipio : str
    DataN : str

# Método construtor, que inicializa as propriedades dos Eleitores
    def __init__(self, titulo : int, nome : str, municipio : str, dataN : str):
        self.Nome = nome
        self.Titulo = titulo
        self.DataN = dataN
        self.Municipio = municipio

   
            
        

