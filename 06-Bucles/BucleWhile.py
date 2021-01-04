""" Bucle While

El bucle while es una estructura de control
que itera o repite la ejecucion de una serie de instrucciones tantas 
veces como sea necesario, hasta que deje de cumplirse la condicion.


wwhile condicion
        bloque de intrucciones
        actualizacion de contador

"""

contador = 0

while contador <= 100:
    print(f"Estoy en el número: {contador} ", end="\t "  )
    contador += 1

    if contador % 4 == 0: 
        print("\n")
