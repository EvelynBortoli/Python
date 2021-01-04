"""
Ejercicio 1:

Crear dos variables
mostrarlas en pantalla
y mostrar el tipo de dato que son

"""

pais = input("\nDe que país eres? ")

ciudad = input("\n\nDe que ciudad eres?")

años = input("\n\nCuantos años tienes? ")


print(f"\n{pais} - {ciudad} - {años}")

print(f"\nPaís: {pais} es del tipo: {type(pais)}")

print(f"\nCiudad: {ciudad} es del tipo: {type(ciudad)}")

print(f"\nAños: {años} es del tipo: {type(años)}")

años = int(años)

print(f"\nDespues de convertirlo, años es del tipo: {type(años)} ")
