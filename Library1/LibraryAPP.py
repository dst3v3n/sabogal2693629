from sys import path

path.append("..\\sabogal2693629")

from Library import *

from Library1.Book import *

obj1 = Library (10 , "La llorona")

obj1.setTitulo("La llorona")

print(obj1.getTitulo ())

obj2 = Book ("La llorona" , "Harold" , 1028 , "10/25/2014")
obj2.setISBN(1028 , "La llorona")