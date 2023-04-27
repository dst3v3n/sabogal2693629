#Solicite un numero positivo al usuario(debe incluirse en la serie). Diga cuantos multiplos de n hay en la serie desde cero hasta el numero ingresado. n se ingresa por teclado tambien.
p=abs(int(input("Digita un numero positivo: ")))
n=abs(int(input("Digita el multiplo: ")))

p+=1

for i in range(0,p,n):
    print(i)