from Book import *
from User import *
from Account import *


obj2 = Book ("La llorona" , "Harold" , 102866 , "10/25/2014" , "Harold")
obj1 = User ("Harold" , 102866)
obj3 = Account ("Harold" , 102866)


obj1.LibroReservado("Harold","La llorona")
obj1.LibroReservado("Harold","La guerra de los cielos" )
obj1.LibroDevuelto("Harold","La llorona")
obj1.LibroDevuelto("Harold","La guerra de los cielos")
obj1.LibroPerdido("Harold"," La llorona")
obj1.LibroPerdido("Harold", "La Guerra de los cielos")
obj1.LibroPerdido("Harold", "La guerra de los cielos")
obj1.LibroPerdido("Harold", "La guerra de los cielos")

print("multa",obj3.calculate_fine(len(obj1._perdido)))

print(obj1.CheckAccount("Harold"))

# print(obj2.AgregarBook())