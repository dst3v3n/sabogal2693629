def divisores (x):
    divi=[]
    nodivi=[]
    for i in range(1,x+1):
        if x%i==0:
            aux=i
            divi.append(aux)
        else:
            aux=i
            nodivi.append(aux)
    return divi

y=int(input("Digita un numero:  "))

print(f"Los numeros divisores son", divisores(y))