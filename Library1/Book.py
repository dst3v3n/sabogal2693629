from Library import *

class Book (Library):
    def __init__(self, Titulo:str , Autor:str , ISBN:str , Publicacion:str):
        self.__titulo = [Titulo]
        self.__autor =  Autor
        self.__isbn = ISBN
        self.__publicacion = Publicacion
        self.__estado = None
        self.__valores = []
        Library.__init__(self , ISBN , Titulo)

    def setISBN (self, isbn, titulo):
        if titulo in self.__titulo:
            

    def AgregarBook (self, Titulo:str , Autor:str , ISBB:str , Publicacion:str):
