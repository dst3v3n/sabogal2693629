#Determinar cuales y cuantos números perfectos hay entre 1 y
#1000?

sum=0
divi=0
cont=0


for i in range(1,1001):
    for j in range(i):
        if j%i==0 and i!=i:
            divi=j
            sum+=j
        if sum-i==divi:
            print(f"{i} Es un numero perfecto")
print(f"El total de numeros perfectos son: {cont}")