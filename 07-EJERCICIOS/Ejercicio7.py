"""
HACER UN EJERCICIO QUE ME MUESTRE TODOS LOS NUMEROS IMPARES
ENTRE DOS QUE ELIJA EL USUARIO

"""
numero1 = int(input("\nIngrese el primer número: "))
numero2 = int(input("\nIngrese el segundo número "))

print(f"\n\nLOS NÚMEROS IMPARES ENTRE {numero1} y {numero2} son:")

numero1 += 1

if numero1 < numero2:
    for numero1 in range(numero1, numero2):
        if numero1 % 2 == 1:
             print(f"{numero1} - ", end="")
        numero1 += 1