from sys import path

path.append("..\\sabogal2693629")

from objetos.Empleado import *

persona1 = Empleado ("Harold" , "ADSO" , 120000)

persona1.getNombre ("Steven")
persona1.getCargo ("Multimedia")
persona1.getSalario (1160000)

print(f"Tu nombre es: {persona1.setNombre}")
print(f"Tu cargo es: {persona1.setCargo}")
print(f"Tu salario es: {persona1.setSalario}")

print(f"Tu salario por hora es: {persona1.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona1.incrementoSalario()}")
print(f"Tu incremento salarial por las hora extras es de :{persona1.hora_extras(1)}")
print(f"Tu sueldo es de: {persona1.sueldo_total()}")




persona2 = Empleado ("Jhonatan" , "Multimedia" , 120000)

persona2.getNombre ("Sabogal")
persona2.getCargo ("Sistemas")
persona2.getSalario (2460000)

print(f"Tu nombre es: {persona2.setNombre}")
print(f"Tu cargo es: {persona2.setCargo}")
print(f"Tu salario es: {persona2.setSalario}")

print(f"Tu salario por hora es: {persona2.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona2.incrementoSalario()}")
print(f"Tu incremento salarial por las hora extras es de :{persona2.hora_extras(2)}")
print(f"Tu sueldo es de: {persona2.sueldo_total()}")



persona3 = Empleado ("Jhonatan" , "Multimedia" , 5000000)

persona3.getNombre ("Sabogal")
persona3.getCargo ("Sistemas")
persona3.getSalario (5500000)

print(f"Tu nombre es: {persona3.setNombre}")
print(f"Tu cargo es: {persona3.setCargo}")
print(f"Tu salario es: {persona3.setSalario}")

print(f"Tu salario por hora es: {persona3.Salario_Hora()}")
print(f"Tu incremento salarial es de: {persona3.incrementoSalario()}")
print(f"Tu sueldo es de: {persona3.sueldo_total()}")

print(persona3.counter)