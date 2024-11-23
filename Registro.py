from tkinter import *
from tkinter import ttk
from Eleitor import *
from CriarTela import *

class Registro(Eleitor, CriarTela):
   def __init__(self, titulo, nome, municipio, dataN):
      super().__init__(titulo, nome, municipio, dataN)