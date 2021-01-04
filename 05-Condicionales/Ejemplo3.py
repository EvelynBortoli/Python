#Ejemplos de if anidados


nombre = input("Nombre: ")

ciudad = input("Ciudad: ")

continente = input("Continente: ")

edad = input("Edad: ")

if int(edad) >= 18 :
    print(f"{nombre} eres mayor de edad.")

    if continente == "Europa":
        print(f"Vale! Eres Europeo, y vives en la ciudad de {ciudad}")

    else:
        print("No eres europeo, por tanto no puedo mostrar la ciudad")


else:
    print(f"{nombre} NO eres mayor de edad.")
