class Persona:
    def __init__ (self, nombre:str, documento:int):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos = []

    def setNombre (self,nombre:str):
        self.__nombre = nombre
    
    def setDocumento (self, documento:int):
        self.__documento = documento
    
    def Cursos (self, cursos:str):
        if cursos not in self.__cursos:
            self.__cursos.append(cursos)
            return self.__cursos
        else:
            return print(f"El curso {cursos} si esta en la lista")
        
    def Consultcursos(self):
        return self.__cursos
    
    def Modificar (self,x,y):
        if x in self.__cursos:
            for i in self.__cursos:
                if i == x:
                    q=self.__cursos.index(i)
                    self.__cursos.pop(q)
                    self.__cursos.insert(q,y)
                    return self.__cursos
        else:
            return print(f"El curso {x} no esta en la lista")
    
    def eliminar (self,x):
        if x in self.__cursos:
            for i in self.__cursos:
                if i == x:
                    self.__cursos.remove(i)
                    return self.__cursos
        else:
            return print(f"El curso {x} no esta en la lista y no puede ser elimnada")

    def getNombre(self):
        return self.__nombre

    def getDocumento (self):
        return self.__documento