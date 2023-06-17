from sys import path

path.append("..\\sabogal2693629")

from herencia.library_python.Book import *
from herencia.library_python.Account import *

class Account:
    def __init__(self, Name:str, ID:int):
        self.__name = Name
        self.__id = ID
        self._reservado = []
        self._devuelto = []
        self._perdido = []
        self._libros = []
        self.__multa = 0
        self.__no_perdido = 0
        self._obj_titulo1 = {Name : []}
        Book.__init__ (self,"La llorona" , "Harold" , 102866 , "10/25/2014" , Name)

    def setMulta (self, Numero:int):
        self.__no_perdido = Numero
        
    def calculate_fine (self):
        self.__multa = (1160000 * 0.3) * self.__no_perdido
        return int(self.__multa)