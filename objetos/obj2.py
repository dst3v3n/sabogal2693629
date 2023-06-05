# class Hola:
#     nombre = None
#     edad = 0
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad

#     def set_nombre(self,nombre):
#         self.nombre = nombre

#     def get_nombre(self):
#         return self.nombre


class futbolista:
    def __init__(self):
        self.__nombre = None
        self.__cantidad_goles = 0

    def set_Nombre(self,nombre):
        self.__nombre = nombre

    def set_cantidad(self, goles):
        self.__cantidad_goles = goles
    
    def get_Nombre(self):
        return self.__nombre

    def get_goles(self):
        return self.__cantidad_goles

James = futbolista()

James.set_Nombre("James")
James.set_cantidad(149)
print(James.get_Nombre())
print(James.get_goles(),"goles anotados")


class EquipoVoleibol:
    def __init__(self):
        self.__nombre = None
        self.__edad = 0
        self.__salto = 0.0

    def set_Nombre(self,nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_salto(self, salto):
        self.__salto = salto    
    
    def get_Nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_salto(self) :
        return self.__salto  


Nishida = EquipoVoleibol()

Nishida.set_Nombre("Nishida Kamado")
Nishida.set_edad(23)
Nishida.set_salto(3.46)
print(Nishida.get_Nombre())
print(Nishida.get_edad())
print(Nishida.get_salto() , "cm")


# objeto = Hola("Harold",18)
# objeto.set_nombre("Torres")
# print(objeto.get_nombre())