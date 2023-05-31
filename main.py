from sys import path

path.append("..\\sabogal2693629\\modulos")
# path.append("C:\sabogal2693629\modulos"


import slz.listas.lista_slz as slzlista
import slz.diccionario.diccio_slz as slzdiccio

lista=slzlista.llenarLista(10,20)
print(lista)

diccio = {}
x = input("Digita la palabra clave: ")
y = input("Digita el valor: ")
print(slzdiccio.updateIngles(diccio,x,y))