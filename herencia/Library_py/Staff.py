from User import *

class Staff(User):
    def __init__ (self, Departamento:str):
        self.__departamento = Departamento

    def setDept (self , Departamento:str):
        self.__departamento = Departamento
    
    @property
    def getDept (self):
        return self.__departamento
    
    