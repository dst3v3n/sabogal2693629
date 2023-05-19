# 2- Hacer diccionarios español ingles, ingles español de animales. Escriba funciones que permitan alimentar estos diccionarios y usarlos. 
# Genere un menú para cada una de las 4 opciones. Alimentar cada diccionario (2 funciones)
# Usar cada diccionario (2 funciones)
def usarEspañol (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def usarIngles (diccionario , x):
    if x in diccionario:
        return diccionario[x]

def updateEspañol(diccio , x , y):
    diccio.update({x : y})
    return diccio

def updateIngles(diccio , x , y):
    diccio.update({x : y})
    return diccio


español = {}
ingles={}


print("1.Mostrar diccionario en Español Ingles")
print("2.Mostrar diccionario en ingles Español")
print("3.Actualizar diccionario de Español")
print("4.Actualizar diccionario de Ingles")
print("5.Usar Diccionario de Español")
print("6.Usar Diccionario de Ingles")

selector = 1

while selector !=0:
    selector = abs(int(input("Digita una opcion: ")))
    match selector:
        case 1:
            print(español)
        case 2:
            print(ingles)
        case 3:
            clave = str(input("Digita la palabra en español que quieres agregar: "))
            valor = str(input("Digita la palabra en ingles que quieres agregar: "))
            print(updateEspañol(español,clave,valor))
        case 4:
            clave = str(input("Digita la palabra en ingles que quieres agregar: "))
            valor = str(input("Digita la palabra en español que quieres agregar: "))
            print(updateIngles(ingles,clave, valor))
        case 5:
            x= input("Ingresa la palabra ")
            print(usarEspañol(español,x))
        case 6:
            x= input("Ingresa la palabra ")
            print(usarIngles(ingles,x)) 