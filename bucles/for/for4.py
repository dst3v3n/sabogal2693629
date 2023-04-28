#Determinar cuales son los numeros divisores ingresados por teclado

x=abs(int(input("Digita un numero: ")))
divi=0
nodivi=0


for i in range(1,x+1):
    if x%i==0:
        divi=i
        print("El numero es divisible", divi)
    else:
        nodivi=i
        print("No es divisible", nodivi)