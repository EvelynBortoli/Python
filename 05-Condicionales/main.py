"""
Condicional if
SI se cumple_esta condicion:
       ejecutar_tal_instruccion
SI NO:
        ejecutar_otro_tipo_de_instruccion
"""
#Ejemplo 1

print("############# Ejemplo 1 ############")

color = input("¿Cual es tu color preferido? ")

print(color)

if color == "rojo":
    print("TU color favorito es rojo")

else:
    print("Tu color favorito no es rojo")