import random 
tam= random.randint(15,20)
lista=[random.randrange(9) for i in range(tam)]
x=1
print(lista)

#lista.sort()

while x<=9:
    x= abs(int(input("Digita un numero de 0 a 9: ")))
    cont=0
    if x in lista:
        print("El numero existe")
        for i in range (len(lista)):
            if i in x==lista:
                cont+=1
    if cont>=2:
        print("El numero esta repetido")
        print(cont)
    else:
        print("El numero no existe")

        




#lista.reverse()