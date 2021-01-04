"""
MOSTRAR LOS CUADRADOS DE LOS PRIMEROS 60 NÚMEROS
con while

"""

num = 1


print("\n++++++++++++++++ A CONTINUACIÓN LOS CUADRADOS DE LOS PRIMEROS 60 NÚMEROS ++++++++++++++++++++\n")

while num <= 60:
    cuadrado = num*num

    print(f"El cuadrado de {num} es {cuadrado}\t", end="")
    if num % 4 == 0:
        print("\n")
    
    num +=1