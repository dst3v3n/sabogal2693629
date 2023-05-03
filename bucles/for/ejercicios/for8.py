#Determinar si dos numeros ingresados son amigos

x= abs(int(input("Digita un numero: ")))
y= abs(int(input("Digita un numero: ")))
sum_x=0
sum_y=0
divi_x=0
divi_y=0

for i in range(1,x+1):
    if x%i==0 and i!=x:
        sum_x+=i

for i in range(1,y+1):
    if y%i==0 and i!=y:
        sum_y+=i

if (sum_y==x and sum_x==y):
    print(f"Los numeros son amigos. Los valores son: {x}={sum_y} y en {y}={sum_x}")
else:
    print(f"No son numeros amigos {x}={sum_y} y en {y}={sum_x}")