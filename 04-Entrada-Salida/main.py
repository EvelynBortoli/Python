#Entrada y salida de datos

nombre = input("¿Cual es tu Nombre?: ")
#Recordar que el imput siempre toma el dato como string

edad = input("¿Cual es tu edad: ")


print(f"Bienvanid@ {nombre}, veo que tienes {edad} años")

print(f"Dentro de 15 años tendrás {int(edad) + 15}")