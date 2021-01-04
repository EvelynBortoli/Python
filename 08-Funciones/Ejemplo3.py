"""
Ejemplo :
definir funcion con pasaje de VARIOS parametros
"""

print("\n------------EJEMPLO 3 ----------")


def muestraTuNombreYEdad(nombre, edad):
    print(f"\nTu nombre es: {nombre}")

    edad = int(edad)

    if edad >18:
        print("Y eres mayor de edad!")




nombre = input("\n\nAhora introduce tu nombre: ")
edad = input("\n\nAhora introduce tu edad: ")

muestraTuNombreYEdad(nombre, edad)