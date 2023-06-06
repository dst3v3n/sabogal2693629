class Empleado:
    counter = 0
    def __init__(self , Nombre:str , Cargo:str ,Salario:int):
        self.__nombre = Nombre
        self.__cargo = Cargo
        self.__salario = Salario
        self.__horas = 0
        Empleado.counter += 1

    def getNombre (self , Nombre:str):
        self.__nombre = Nombre
        
    def getCargo (self , Cargo:str):
        self.__cargo = Cargo
    
    def getSalario (self , Salario:int):
        self.__salario = Salario

    def setNombre (self):
        return self.__nombre
    
    def setCargo (self):
        return self.__cargo
    
    def setSalario (self):
        return self.__salario
    
    def Salario_Hora (self):
        hora = self.__salario/(47*4)
        return int(hora)

    def incrementoSalario (self):
        if self.__salario == 1160000:
            ipc = 0.1312 + 0.03
            incremento = self.__salario * ipc
            total_incremento = self.__salario + incremento
            return int(total_incremento)
        else: 
            total_incremento = self.__salario * 0.1312
            return int(total_incremento)
        
    def hora_extras (self, Horas:int =0):
        self.__horas = Horas
        incremento = Empleado.incrementoSalario(self)
        salario = Empleado.Salario_Hora(self)
        extras = salario * Horas
        total = incremento + extras
        return int(total)
    
    def sueldo_total (self):
        total = Empleado.hora_extras(self , self.__horas)
        return total