# Codifique funciones para alamacenar en tuplas de cada diccionario todos los animales en español y en ingles respectivamente.

def usarEspañol (diccionario , x ):
    if x in diccionario:
        return diccionario[x]


def usarIngles (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def updateEspañol(diccio , x , y ):
    diccio.update({x : y})
    return diccio

def updateIngles(diccio , x , y):
    diccio.update({x : y})
    return diccio


def tuplaEspañol(tupla,x):
    tupla = tupla + (x,)
    print(tupla)
    return tupla

def tuplaIngles(tupla,x):
    tupla = tupla + (x,)
    return tupla


español = {}
ingles={}
spanish = ()
english = ()


print("1.Mostrar diccionario en Español Ingles")
print("2.Mostrar diccionario en ingles Español")
print("3.Agregar diccionario de Español")
print("4.Agregar diccionario de Ingles")
print("5.Usar Diccionario de Español")
print("6.Usar Diccionario de Ingles")

selector = 1

while selector !=0:
    selector = abs(int(input("Digita una opcion: ")))
    match selector:
        case 1:
            print(español)
            print(spanish)
        case 2:
            print(ingles)
            print(english)
        case 3:
            clave = str(input("Digita la palabra en español que quieres agregar: "))
            valor = str(input("Digita la palabra en ingles que quieres agregar: "))
            print(updateEspañol(español,clave,valor))
            spanish=tuplaEspañol(spanish,clave)
        case 4:
            clave = str(input("Digita la palabra en ingles que quieres agregar: "))
            valor = str(input("Digita la palabra en español que quieres agregar: "))
            print(updateIngles(ingles,clave, valor))
            english=tuplaEspañol(english,clave)
        case 5:
            x= input("Ingresa la palabra ")
            print(usarEspañol(español,x))
        case 6:
            x= input("Ingresa la palabra ")
            print(usarIngles(ingles,x)) 