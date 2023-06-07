from sys import path

path.append("..\\sabogal2693629")

from objetos.Empleado import *

persona1 = Empleado ("Harold" , "ADSO" , 120000)

persona1.setNombre ("Steven")
persona1.setCargo ("Multimedia")
persona1.setSalario (1160000)

print(f"Tu nombre es: {persona1.getNombre}")
print(f"Tu cargo es: {persona1.getCargo}")
print(f"Tu salario es: {persona1.getSalario}")

print(f"Tu salario por hora es: {persona1.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona1.incrementoSalario()}")
print(f"Tu incremento salarial por las hora extras es de :{persona1.hora_extras(1)}")
print(f"Tu sueldo es de: {persona1.sueldo_total()}")




persona2 = Empleado ("Jhonatan" , "Multimedia" , 120000)

persona2.setNombre ("Sabogal")
persona2.setCargo ("Sistemas")
persona2.setSalario (2460000)

print(f"Tu nombre es: {persona2.getNombre}")
print(f"Tu cargo es: {persona2.getCargo}")
print(f"Tu salario es: {persona2.getSalario}")

print(f"Tu salario por hora es: {persona2.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona2.incrementoSalario()}")
print(f"Tu incremento salarial por las hora extras es de :{persona2.hora_extras(2)}")
print(f"Tu sueldo es de: {persona2.sueldo_total()}")



persona3 = Empleado ("Jhonatan" , "Multimedia" , 5000000)

persona3.setNombre ("Sabogal")
persona3.setCargo ("Sistemas")
persona3.setSalario (5500000)

print(f"Tu nombre es: {persona3.getNombre}")
print(f"Tu cargo es: {persona3.getCargo}")
print(f"Tu salario es: {persona3.getSalario}")

print(f"Tu salario por hora es: {persona3.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona3.incrementoSalario()}")
print(f"Tu sueldo es de: {persona3.sueldo_total()}")

print(persona3.counter)