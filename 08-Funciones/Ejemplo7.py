"""
EJEMPLO 7

funcion dentro de otra funcion

"""

print("\n····················EJEMPLO 7 ·················\n")

def getNombre(nombre):
    texto= f"El nombre del usuario es: {nombre}"
    return texto

def getApellido(apellido):
    texto = f" y su apellido es: {apellido}"
    return texto


def nombreCompleto(nombre, apellido):
    texto = getNombre(nombre) + getApellido(apellido)

    return texto

nombre = input("Introduce tu nombre: ")
apellido = input("Introdice tu apellido: ")
print(nombreCompleto(nombre, apellido))
