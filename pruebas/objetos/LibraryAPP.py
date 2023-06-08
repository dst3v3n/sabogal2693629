from sys import path

path.append("..\\sabogal2693629")

from herencia.Library_py.book import *
from herencia.Library_py.User import *
from herencia.Library_py.Account import *

prueba1 = Book("La Guerra De Los Cielos" , "Fernando Trujillo" , 978-958-30-6050-2 , 10/2/2021, "Disponible")

prueba1.append_duet ("La Guerra De Los Cielos" , "Cesar Garcia")

print(prueba1.reservation_status ("La Guerra De Los Cielos"))

prueba1.feedback("La Guerra De Los Cielos")
print(prueba1.Book_request("La Guerra De Los Cielos"))


print(prueba1.renw_info("La Guerra De Los Cielos"))

prueba1 = Account ("Hola" , "mundo" , "X")
prueba1.setMulta_Cantidad(48)
prueba1 = User("Harold",10 )
prueba1.verify("Harold", 10)
prueba1.CheckAcount("Harold" , 10)