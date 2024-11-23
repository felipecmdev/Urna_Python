from CriarTela import *

class Urna(CriarTela):
    
    def __init__(self, root):
        super().__init__(root)

        self.label_titulo = ttk.Label(self.frm, text="Urna")
        self.label_titulo.grid(column=0, row=0, columnspan=3, pady=10)

    def adcionarVoto(self, num):
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
app = CriarTela(root)
root.mainloop()