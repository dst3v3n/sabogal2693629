from User import *

class Staff (User):
    def __init__(self, Dept:str):
        self.__dept = Dept

    def setDept (self , Dept:str):
        self.__dept = Dept
    
    def getDept (self):
        return self.__dept