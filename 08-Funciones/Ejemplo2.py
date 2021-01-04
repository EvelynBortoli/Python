"""
Ejemplo 2:
definir funcion con pasaje de parametros
"""

print("\n------------EJEMPLO 2 ----------")


def muestraTuNombre(nombre):
    print(f"\nTu nombre es: {nombre}")


muestraTuNombre("Mariano")
muestraTuNombre("Piero")
muestraTuNombre("Yamile")

nombre = input("\n\nAhora introduce tu nombre:")

muestraTuNombre(nombre)