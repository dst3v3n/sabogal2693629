from herencia.Library_py.Account import *
from herencia.Library_py.book import *


class User:
    def __init__(self, Name:str, ID:int):
        self.__name = Name
        self.__id = ID
        self.__reservado=[]
        self.__devueltos=[]
        self.__multa = 0
        Account.__init__ (self, self.__reservado , self.__devueltos)
        Book.__init__ (self,"La Guerra De Los Cielos" , "Fernando Trujillo" ,9789583060502 , "10/02/2021", "Disponible")

    # def retornos (self, Titulos:)


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
            return "No estas verificado"
    
    def CheckAcount (self, Nombre , Documento):
        if User.verify (self , Nombre , Documento) == "Verificado":
            self.__reservado.append (input ("Digita el titulo reservado: "))
            self.__devueltos.append(input ("Digita el titulo devueltos : "))
            perdido = int(input ("Digita el numero de libros que haz perdido: "))
            Account.setLibros_Perdidos = perdido
            obj1 = Account (self.__reservado,self.__devueltos)
            self.__multa=obj1.calculate_fine (perdido)
            return self.__reservado, self.__devueltos, self.__multa
    
    def get_book_info(self,Titulo):
        Book.renw_info(self,Titulo)