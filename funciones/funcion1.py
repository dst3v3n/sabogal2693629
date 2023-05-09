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
    print(f"El numeros divisibles de {x} son: {divi}")
    print(f"Los numeros no divisibles de {x} son: {nodivi}")



divisores(10)
divisores(50)
divisores(19)
divisores(35)

