"""
Ejemplo :
definir funcion con pasaje de VARIOS parametros opcionales
"""

print("\n------------EJEMPLO 4 ----------")

def getEmpleado ( nombre, dni = None):

    print(f"Empleado:\nNombre: {nombre}")
    if dni != None and dni != "\n": 
        print(f"DNI: {dni}")


nombre = input("Introducir nombre de empleado: ")

dni = input("Introducir DNI empleado: ")
getEmpleado(nombre)
