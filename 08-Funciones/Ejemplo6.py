"""
Ejemplo 6
calculadora

"""

print("···················Ejemplo 6 ·····················\n")
print("..................CALCULADORA......................\n")

def calculadora(numero1, numero2, operacion = False):
    suma = numero1 + numero2
    resta =numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    if operacion == "Todas" or operacion == "todas":
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
        cadena += "Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena += "Division: " + str(division)
    else: 
        if operacion == "suma":
             cadena += "Suma: " + str(suma)
             cadena += "\n"
        if operacion == "resta":
             cadena += "Resta: " + str(resta)
             cadena += "\n"
        if operacion == "Multiplicacion":
             cadena += "Multiplicacion: " + str(multiplicacion)
             cadena += "\n"
        if operacion == "Division": 
             cadena += "Division: " + str(division)

    return(cadena)

numero1 = int(input("Ingrese el primer número con el que desea operar: "))
numero2 = int(input("Ingrese el segundo número con el que desea operar: "))
operacion = input("Ingrese la operacion a efectuar: ")
print(calculadora(numero1, numero2, operacion))
