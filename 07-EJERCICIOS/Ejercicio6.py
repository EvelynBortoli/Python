"""
MOSTRAR TODAS LAS TABLAS DE MULTIPLICAR
DEL UNO AL DIEZ
"""


cont1= 0



for cont1 in range(0, 11):
    print(f"\nLa tabla del {cont1} es:\n")
    cont2 = 0
    for cont2 in range(0, 11):
        print(f"{cont1} x {cont2} = {cont1*cont2}")
        cont2 += 1
    cont1 += 1
