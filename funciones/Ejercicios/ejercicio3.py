# Llenar un arreglo de n elementos con números generados con la función random. No
# puede haber números repetidos. Si intenta ingresar al arreglo un número que ya existe,
# imprimirlo para anunciar que ese número ya está en el arreglo.
import random
def arreglo (lista):
    tam=random.randint(15,25)
    cont=0
    for i in range(tam):
        while cont!=tam:
            num=int(random.randrange(120))
            if num not in lista:
                lista.append(num)
                cont+=1
        return lista

def introducir(lista,x):
    if x not in lista:
        lista.append(x)
    else:
        print(f"El numero {x} ya esta en la lista")
    return lista

aleatorio=[]
print(arreglo(aleatorio))
num=1
while num!=0:
    num=abs(int(input("Digita un numero que quieres ingresar a la lista: ")))
    print(introducir(aleatorio,num))
