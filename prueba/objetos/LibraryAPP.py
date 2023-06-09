from sys import path

path.append("..\\sabogal2693629")

from herencia.Library_py.book import *
from herencia.Library_py.User import *
from herencia.Library_py.Account import *


prueba1 = Book("La Guerra De Los Cielos" , "Fernando Trujillo" , 9789583060502 , "10/02/2021", "Disponible")
prueba2 = User ("Harold" , 10)
prueba3 = Account ("La Guerra De Los Cielos" , "Mundo")

print(prueba1.append_duet ("La Guerra De Los Cielos" , "Cesar Garcia"))
print(prueba1.reservation_status ("La Guerra De Los Cielos"))
prueba1.feedback("La Guerra De Los Cielos")
print(prueba1.Book_request("La Guerra De Los Cielos"))
prueba1.renw_info("La Guerra De Los Cielos")

print(prueba2.verify("Harold", 10))
print(prueba2.CheckAcount("Harold" , 10))
prueba2.get_book_info("La Guerra De Los Cielos")