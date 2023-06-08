from herencia.Library_py.book import *
from herencia.Library_py.Account import *


class User:
    def __init__(self, Name:str, ID:int):
        self.__name = Name
        self.__id = ID
        Account.__init__(self,Name ,ID)

    def setNombre (self, Nombre:str):
        self.__name = Nombre
    
    def setID (self, ID:int):
        self.__id = ID

    @property 
    def getNombre (self):
        return self.__name
    
    @property
    def getID (self):
        return self.__id
    
    def verify (self, Nombre:str, Documento:int):
        if Nombre == self.__name and Documento == self.__id:
            return "Verificado"
        else: 
            print("No estas verificado")
    
    def CheckAcount (self, Nombre , Documento):
        if User.verify (self , Nombre , Documento) == "Verificado":
            print(Account.getLibros_Prestados)
            print(Account.getLibros_Reservados)
            print(Account.getLibros_Devueltos)
            print(Account.getLibros_Perdidos)
            print(Account.calculate_fine)