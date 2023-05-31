from sys import path

path.append("..\\sabogal2693629\\modulos")

import MABE.Diccionario.funtion as mabe_diccio
import MABE.Listas.funcion as mabe_lista

diccio = {}
print(mabe_diccio.alimentar_diccionario_esp_ingles(diccio))
print(mabe_lista.llenarLista(20,35))