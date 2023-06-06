from sys import path

path.append("..\\sabogal2693629")

from objetos.Empleado import *

persona1 = Empleado ("Harold" , "ADSO" , 120000)

persona1.getNombre ("Steven")
persona1.getCargo ("Multimedia")
persona1.getSalario (1160000)

print(persona1.setNombre)
print(persona1.setCargo)
print(persona1.setSalario)

print(persona1.Salario_Hora())
print(persona1.incrementoSalario())
print(persona1.hora_extras(2))
print(persona1.sueldo_total())




persona2 = Empleado ("Jhonatan" , "Multimedia" , 120000)

persona2.getNombre ("Sabogal")
persona2.getCargo ("Sistemas")
persona2.getSalario (2460000)

print(persona2.setNombre)
print(persona2.setCargo)
print(persona2.setSalario)

print(persona2.Salario_Hora())
print(persona2.incrementoSalario())
print(persona2.hora_extras(1))
print(persona2.sueldo_total())




persona3 = Empleado ("Jhonatan" , "Multimedia" , 5000000)

persona3.getNombre ("Sabogal")
persona3.getCargo ("Sistemas")
persona3.getSalario (5500000)

print(persona3.setNombre)
print(persona3.setCargo)
print(persona3.setSalario)

print(persona3.Salario_Hora())
print(persona3.incrementoSalario())
print(persona3.sueldo_total())

print(persona3.counter)