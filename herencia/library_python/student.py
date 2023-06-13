from User import *

class Student (User):
    def __init__(self, Class:str):
        self.__class = Class

    def setClass (self , Class:str):
        self.__class = Class
    
    def getClass (self):
        return self.__class