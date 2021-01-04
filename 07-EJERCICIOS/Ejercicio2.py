"""
MOSTRAR POR PANTALLA TODOS LOS NUMEROS
PARES DESDE EL 0 HASTA EL 120
"""

cont = 1
print("\n +++++++++++++++ MOSTRAR LOS NUMEROS PARES DESDE EL 1 HASTA EL 120 ++++++++++++++\n")
for cont in range(1, 121):
    if cont % 2 == 0:
        print(f"{cont}\t", end="")
    if cont % 20 == 0:
        print("\n")
    cont += 1