from sys import path

path.append("..\\sabogal2693629")

from herencia.library_python.Account import *
from herencia.library_python.Book import *


class User(Account):
    def __init__(self , Name:str , ID:int):
        self._name = Name
        self.__id = ID
        self.__verificado = None
        Account.__init__(self , Name , ID)
        Book.__init__(self , "La llorona" , "Harold" , 102866 , "10/25/2014" , "Harold")

    def verify (self , Name:str, ID:int):
        if self._name == Name and self.__id == ID:
            self.__verificado = "Verificado"
            return "Verificado"
        else:
            self.__verificado = "No Verificado"
            return "No Verificado"
            
    def LibroReservado (self ,Name:str , Titulo:str):
        self._reservado.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        
    def LibroDevuelto (self ,Name:str , Titulo:str):
        self._devuelto.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        
    def LibroPerdido (self , Name:str, Titulo:str):
        self._perdido.append(Titulo)
        self._libros.append (Titulo)
        del self._obj_titulo1[Name]
        self._obj_titulo1.update ({Name : self._libros + [Titulo]})
        Book.Obj_Libro(self,Name,Titulo)
        self.setMulta(len(self._perdido))

    def CheckAccount (self, Name:str):
        return self._obj_titulo1[Name]
        
    # def get_book_info (self , Titulo:str , informacion):
    #     self.__informacion = informacion
    #     print(self.__informacion)