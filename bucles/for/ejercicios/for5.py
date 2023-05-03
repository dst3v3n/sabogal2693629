#Determinar si un numero es o no es primo

x=abs(int(input("Digita un numero: ")))
divi=0
nodivi=0
cont=0
primo=0

for i in range(1,x+1):
    if x%i==0:
        divi=i
        cont+=1
if cont<=2:
    primo=cont
    print("El numero es primo")
else:
     print("El numero no es primo")
print(f"Se puede dividir en {cont} numeros")