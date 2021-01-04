""" 
FOR

for variable in elemento_iterable (lista, rango, etc)
        BLOQUE DE INSTRUCCIONES

"""

cont = 0
resultado=0

for cont in range(0, 10):
    print(f"Voy por el {cont}")
    resultado +=cont

print(f"El resultado de la suma anterior es: {resultado}")