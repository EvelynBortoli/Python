"""
Pedir indefinidamente un numero
hasta que el usuario ingrese 111 para salir

"""

numero=int(input("Ingrese un número, si desea salir ingrese 111: "))

while numero != 111:
    print(f"\nEl número que ingresó es: {numero}")
    numero=int(input("\nIngrese un número, si desea salir ingrese 111: "))

print("\nPresionó 111, ha decidido salir. \nQue pase un buen día!")