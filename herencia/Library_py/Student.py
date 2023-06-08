from User import *

class Staff(User):
    def __init__ (self, Class:str):
        self.__class = Class

    def setClass (self , Class:str):
        self.__class = Class
    
    @property
    def getClass (self):
        return self.__class
    
