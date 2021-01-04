"""
MOSTRAR LOS CUADRADOS DE LOS PRIMEROS 60 NÚMEROS 
con un bucle for

"""

num = 1


print("\n++++++++++++++++ A CONTINUACIÓN LOS CUADRADOS DE LOS PRIMEROS 60 NÚMEROS ++++++++++++++++++++\n")

for num in range(1, 61):
    cuadrado = num*num

    print(f"El cuadrado de {num} es {cuadrado}\t", end="")
    if num % 4 == 0:
        print("\n")
    
    num +=1