colores={
    "rojo": "red",
    "azul": "blue",
    "naranja": "orange",
    "negro": "black",
    "blanco": "white",
    "amarrillo": "yellow",
    "morado": "purple",
    "rosado": "pink",
    "cafe": "brown",
    "verde": "green",
}


lista=["Blanco", "cafe", "azules", "azul", "naranja", "negro", "blanco", "amarrillo"]

for x in lista:
    if x in colores:
        print(f"El color {x} en ingles se escribe {colores[x]}")
    else:
        print(f"{x} no esta en el diccionario")