"""
HACER QUE MUESTRE EN PANTALLA LS NUMEROS QUE HAY
ENTRE DOS NUMEROS QUE ME DIGA EL USUARIO
"""

numero1 = int(input("\nIngresar el primer número: "))

numero2 = int(input("\nIngresar el segundo número: "))

numero1 +=1

if numero1 < numero2:
    for numero1 in range(numero1, numero2):
        print(f"{numero1} - " , end="")
        numero1 +=1

else:
    print("RANGO INVALIDO")