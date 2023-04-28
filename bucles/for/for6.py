"""Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este"""

x=abs(int(input("Digita un numero: ")))
sum=0
divi=0
primo=0

for i in range(1,x+1):
    if x%i==0 and i!=x:
        divi=i
        sum+=i
if sum==x:
    print(f"Los numeros divisores son: {divi}")
    print(f"{x} Es un numero perfecto")
else:
    print(f"No es un numero perfecto: {sum}")
            