### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre" : "Harold", "Apellido" : "Sabogal", "Edad" : 18, 1 : "Python"}

my_dict = {"Nombre" : "Harold", 
           "Apellido" : "Sabogal", 
           "Edad" : 18, 
           "Lenguajes" : {"Python" , "JavaScript", "Java"},
            1 : 1.79
           }

print(my_dict)
print(my_other_dict )

print(len(my_dict))
print(len(my_other_dict))

print(my_dict["Nombre"]) 

my_dict["Calle"] = "Calle Sabogal"
print(my_dict)

print(my_dict[1]) 

del my_dict["Calle"]
print(my_dict)

print("Harold" in my_dict)
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys()) #Retorna todas las keys
print(my_dict.values()) #Retorna todos los valores

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))  #Se crea un diccionaro sin los valores
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict) 

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

# my_new_dict = dict.fromkeys(my_dict,["Harold","Sabogal"])
print(my_new_dict)

my_values = my_new_dict.values() #dict_values
print(type(my_values)) 

print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))